class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = 0
        seen = {0}
        res = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - target in seen:
                seen = {prefix_sum}
                res += 1
            seen.add(prefix_sum)
        return res
