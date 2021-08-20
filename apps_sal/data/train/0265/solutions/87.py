class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        subarrays = []
        summ = 0
        lookup = set()
        count = 0
        lookup.add(0)
        for num in nums:
            summ += num
            if summ - target in lookup:
                count += 1
                summ = 0
                lookup = set([0])
            else:
                lookup.add(summ)
        return count
