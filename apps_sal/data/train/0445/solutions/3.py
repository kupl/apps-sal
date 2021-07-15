class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #0,1,4,5,10
        N = len(nums)-1
        if N < 3:
            return 0
        minVal = 2**32
        nums.sort()
        
        for i in range(4):
            minVal = min(minVal, nums[N-3+i]-nums[i])
            
        return minVal
