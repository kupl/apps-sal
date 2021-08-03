class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7

        total = sum([1 if c == '1' else 0 for c in s])
        if total == 0:
            n = len(s) - 1
            return (n * (n - 1) // 2) % MOD  # nCr combinatorial formula
        if total % 3 > 0:
            return 0

        x = total // 3
        count = 0
        zero1 = 0
        zero2 = 0
        for i, c in enumerate(s):
            if c == '1':
                count += 1
            if c == '0' and count == x:
                zero1 += 1
            elif c == '0' and count == 2 * x:
                zero2 += 1

        ans = (zero1 + 1) * (zero2 + 1)
        return ans % MOD
