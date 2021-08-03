class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maxes = [0, 0, 0, 0]
        for num in nums:
            new_maxes = [x for x in maxes]
            for module in maxes:
                idx = (num + module) % 3
                new_maxes[idx] = max(new_maxes[idx], num + module)
            maxes = new_maxes
        return maxes[0]
