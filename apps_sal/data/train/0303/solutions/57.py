class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        def helper(index, start, mx):
            key = (index, start, mx)
            if key in d:
                return d[key]
            if index == len(arr):
                return (index - start) * mx

            if index - start + 1 <= k:
                d[key] = max(helper(index + 1, start, max(arr[index], mx)), (index - start) * mx + helper(index + 1, index, arr[index]))
                return d[key]
            d[key] = (index - start) * mx + helper(index + 1, index, arr[index])
            return d[key]
        d = dict()
        return helper(0, 0, arr[0])
