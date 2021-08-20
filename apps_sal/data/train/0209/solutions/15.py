class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        if (n - 1) % (K - 1) is not 0:
            return -1
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]

        @lru_cache(None)
        def dp(i, j, k):
            if i == j:
                return 0 if k == 1 else inf
            if k == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min((dp(i, m, 1) + dp(m + 1, j, k - 1) for m in range(i, j)))
        return dp(0, n - 1, 1)
