class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(set(s)) == 1:
            return s
        x = max(s)
        n = len(s)
        res = []
        for i in range(n - 1, -1, -1):
            if res and s[i] == x:
                k = 0
                while k < len(res[-1]) and res[-1][k] == s[i + k]:
                    k += 1
                if k < len(res[-1]) and res[-1][k] < s[i + k]:
                    res[-1] = s[i:]
                elif k == len(res[-1]):
                    res[-1] = s[i:]
            elif s[i] == x:
                res.append(s[i:])
        return res[-1]
