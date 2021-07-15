class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=4: return 0
        
        nums.sort()
        res = float('inf')
        for i in range(4):
            l = nums[i]
            r = nums[n-1-3+i]
            res = min(nums[n-1-3+i]-nums[i], res)
        return res
