class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min((dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j)))
        res = dp(0, n - 1, 1)
        return res if res < inf else -1
