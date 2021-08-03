class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @lru_cache(None)
        def helper(index, start, mx):
            if index == len(arr):
                return (index - start) * mx

            if index - start + 1 <= k:
                return max(helper(index + 1, start, max(arr[index], mx)), (index - start) * mx + helper(index + 1, index, arr[index]))

            return (index - start) * mx + helper(index + 1, index, arr[index])

        return helper(0, 0, arr[0])
