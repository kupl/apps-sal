from bisect import bisect_left, bisect_right


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        n = len(A)
        ret = 0

        # F[i] number of subsequences accept A[i] as minimun
        # G[i] number of subsequences accept A[i] as maximum
        # result = (-F[i] + G[i]) * A[i]

        A.sort()
        MOD = 10 ** 9 + 7

        @lru_cache
        def bimod(n):
            if n == 0:
                return 1
            di = bimod(n // 2)
            if n % 2 == 0:
                return di * di % MOD
            return di * di * 2 % MOD

        @lru_cache
        def nonempty(n):
            return bimod(n) - 1

        i = 0
        while i < n:
            j = i
            while j < n and A[j] == A[i]:
                j += 1
            se = j - i
            sl = i
            sr = n - j

            ret = (ret + A[i] * nonempty(se) * (nonempty(sl) - nonempty(sr)) % MOD) % MOD
            i = j

        return ret
