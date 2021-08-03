class Solution:
    def numWays(self, s: str) -> int:
        if not s or len(s) < 3 or s.count('1') % 3 != 0:
            return 0

        mod = pow(10, 9) + 7
        n = s.count('1')
        if n == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % mod

        c1, c2, i = 0, 0, 0
        for ch in s:
            if ch == '1':
                i += 1
            elif ch == '0' and n / 3 <= i < n / 3 + 1:
                c1 += 1
            elif ch == '0' and n * 2 / 3 <= i < n * 2 / 3 + 1:
                c2 += 1
        return (c1 + 1) * (c2 + 1) % mod
