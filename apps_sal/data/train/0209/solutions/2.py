class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:

        @lru_cache(None)
        def recursive(i, j, piles):
            if j - i + 1 < K:
                return 0
            if piles == 1:
                return recursive(i, j, K) + pre_sum[j + 1] - pre_sum[i]
            else:
                min_cost = float('inf')
                for k in range(i, j, K - 1):
                    min_cost = min(min_cost, recursive(i, k, 1) + recursive(k + 1, j, piles - 1))
                return min_cost
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + stones[i]
        return recursive(0, n - 1, 1)
