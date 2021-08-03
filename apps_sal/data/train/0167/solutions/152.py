from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(maxsize=None)
        def dp(K: int, N: int) -> int:
            if N == 0:
                return 0
            elif K == 1:
                return N
            else:
                l, r = 1, N
                res = N
                while l + 1 < r:
                    X = (l + r) // 2
                    f1 = dp(K, N - X)
                    f2 = dp(K - 1, X - 1)
                    if f1 < f2:
                        r = X
                    elif f1 == f2:
                        l = r = X
                    else:
                        l = X
                return 1 + min(max(dp(K - 1, X - 1), dp(K, N - X)) for X in (l, r))
        return dp(K, N)
