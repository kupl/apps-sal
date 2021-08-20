class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = count = 0
        seen = {0}
        for num in nums:
            prefix_sum += num
            if prefix_sum - target in seen:
                prefix_sum = 0
                count += 1
                seen = set([0])
            seen.add(prefix_sum)
        return count
