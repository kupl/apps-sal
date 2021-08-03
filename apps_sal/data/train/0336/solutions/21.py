class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = collections.Counter(s)
        req = 0
        for i in t:
            if i not in count:
                req += 1
            else:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        if count:
            return req
        else:
            return 0
