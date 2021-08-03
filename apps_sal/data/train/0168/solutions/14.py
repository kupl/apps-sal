class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        d = {}
        for c in list(s):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        print(d)

        if len(list(d.keys())) == k:
            return True
        else:
            odds = 0
            for v in list(d.values()):
                if v % 2 == 1:
                    odds += 1

            return False if odds > k else True
