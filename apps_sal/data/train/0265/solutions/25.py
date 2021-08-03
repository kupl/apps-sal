class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = count = 0
        prev_subarray_end = -1
        seen = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            if seen.get(prefix_sum - target, -2) >= prev_subarray_end:
                count += 1
                prev_subarray_end = i
            seen[prefix_sum] = i
        return count
