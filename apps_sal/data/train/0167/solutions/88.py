class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[K, N]
            res = float('inf')
            (low, high) = (1, N + 1)
            while low < high:
                mid = (low + high) // 2
                broken = dp(K - 1, mid - 1)
                notBroken = dp(K, N - mid)
                if broken > notBroken:
                    high = mid
                    res = min(broken + 1, res)
                else:
                    low = mid + 1
                    res = min(notBroken + 1, res)
            memo[K, N] = res
            return res
        return dp(K, N)
