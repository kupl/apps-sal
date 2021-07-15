class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        h = {0: 1}
        summ = count = 0
        for i in range(0, len(nums)):
            summ += nums[i]
            if summ - target in h:
                count += 1
                h = {}
            h[summ] = i
            
        return count

