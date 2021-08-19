class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        table = dict()

        def dp(K: int, N: int) -> int:
            if K == 1:
                return N
            if N <= 0:
                return 0
            if (K, N) in table:
                return table[K, N]
            lo = 1
            hi = N
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                up = dp(K, N - mid)
                dn = dp(K - 1, mid - 1)
                if up >= dn:
                    lo = mid + 1
                else:
                    hi = mid - 1
            table[K, N] = 1 + min(dp(K, N - hi), dp(K - 1, lo - 1))
            return table[K, N]
        return dp(K, N)
