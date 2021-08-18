class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        res = 1
        seen = set()
        for m in range(1, 1 << (n - 1)):
            if bin(m).count('1') < res:
                continue
            valid = True
            p = 0
            for i in range(1, n + 1):
                if valid:
                    if m & (1 << (i - 1)) or i == n:
                        if s[p:i] in seen:
                            valid = False
                        seen.add(s[p:i])
                        p = i
            if valid:
                res = max(res, len(seen))
            seen = set()
        return res
