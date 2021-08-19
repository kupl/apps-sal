class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        max_3 = sorted(nums[:4], reverse=True)
        min_3 = sorted(nums[:4])
        for i in range(4, len(nums)):
            max_3.append(nums[i])
            max_3.sort(reverse=True)
            max_3.pop()
            min_3.append(nums[i])
            min_3.sort()
            min_3.pop()
        return min([max_3[i] - min_3[3 - i] for i in range(4)])
