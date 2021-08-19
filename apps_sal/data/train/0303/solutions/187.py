class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        def max_sum(idx):
            if idx >= len(arr):
                return 0
            if idx in memo:
                return memo[idx]
            subarr_max = float('-inf')
            options = []
            for end in range(idx, min(idx + k, len(arr))):
                subarr_max = max(subarr_max, arr[end])
                subarr_sum = subarr_max * (end - idx + 1)
                options.append(subarr_sum + max_sum(end + 1))
            memo[idx] = max(options)
            return memo[idx]
        return max_sum(0)
