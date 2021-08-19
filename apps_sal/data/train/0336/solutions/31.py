class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        a = s
        b = t
        if len(s) == 0:
            return len(t)
        if len(t) == 0:
            return len(s)
        for curr in a:
            # print(\"Curr=\",curr,\"and t=\",b)
            if curr in b:
                b = b.replace(curr, '', 1)
                # print(\"Now t=\",b)
            else:
                count += 1
        return count
