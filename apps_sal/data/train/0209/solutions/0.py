class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        prefix = [0]
        for s in stones:
            prefix.append(prefix[-1] + s)
        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K:
                return 0
            res = 0
            if (j - i) % (K - 1) == 0:
                res = prefix[j+1] - prefix[i]
            return res + min(dp(i, mid) + dp(mid+1, j) for mid in range(i, j, K - 1))
        return dp(0, n - 1)
