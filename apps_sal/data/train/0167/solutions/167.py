class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}

        def helper(K, N):
            if N <= 2:
                return N
            if K == 1:
                return N
            if (K, N) not in dp:
                l = 1
                r = N
                while l + 1 < r:
                    mid = (l + r) // 2
                    die = helper(K - 1, mid - 1)
                    live = helper(K, N - mid)
                    if die < live:
                        l = mid
                    elif die > live:
                        r = mid
                    else:
                        l = r = mid
                dp[K, N] = 1 + min([max(helper(K - 1, l - 1), helper(K, N - l)), max(helper(K - 1, r - 1), helper(K, N - r))])
            return dp[K, N]
        return helper(K, N)
