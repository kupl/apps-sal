class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]
            low, high = 1, N + 1
            while low < high:
                mid = (low + high) // 2
                broken = dp(K - 1, mid - 1)
                notBroken = dp(K, N - mid)
                if broken >= notBroken:
                    high = mid
                else:
                    low = mid + 1
            memo[(K, N)] = 1 + max(dp(K - 1, low - 1), dp(K, N - low))
            return memo[(K, N)]
        return dp(K, N)
