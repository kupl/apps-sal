class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        existingSums = set([0])
        prefixsum = 0
        count = 0
        for num in nums:
            prefixsum += num
            if prefixsum - target in existingSums:
                count += 1
                existingSums = set([0])
                prefixsum = 0
            existingSums.add(prefixsum)
        return count
