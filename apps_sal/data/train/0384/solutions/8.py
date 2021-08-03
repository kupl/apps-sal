from collections import deque


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        n = len(A)

        MOD = 10 ** 9 + 7

        pows = [1] * n
        for i in range(1, n):
            pows[i] = (pows[i - 1] * 2) % MOD

        A.sort()
        ans = 0

        for i, v in enumerate(A):
            ans += pows[i] * v - pows[n - 1 - i] * v
            ans %= MOD

        return ans % MOD
