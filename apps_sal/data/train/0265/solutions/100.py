class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        map = {0: -1}
        (prefix, rightmost, count) = (0, -1, 0)
        for (i, val) in enumerate(nums):
            prefix += val
            if prefix - target in map and map[prefix - target] >= rightmost:
                count += 1
                rightmost = i
            map[prefix] = i
        return count
