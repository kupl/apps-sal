class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        numsLen = len(nums)
        oldSum = sum([abs(nums[i] - nums[i+1]) for i in range(numsLen-1)])
        if numsLen < 3:
            return oldSum
        
        delta = 0
        for i in range(1, numsLen-1):
            delta = max(delta, abs(nums[i + 1] - nums[0]) - abs(nums[i+1] - nums[i]), abs(nums[-1] - nums[i-1]) - abs(nums[i]-nums[i-1]))
        
        high = float('-inf')
        low = float('inf')
        
        for x, y in zip(nums, nums[1:]):
            high = max(high, min(x, y))
            low = min(low, max(x, y))
        
        return oldSum + max(delta, (high-low)*2)
        
#         numsLen = len(nums)
        
#         def findDelta(l, r):
#             if l == 0 and r == numsLen-1:
#                 return 0
#             if l == 0:
#                 return abs(nums[r + 1] - nums[l]) - abs(nums[r+1] - nums[r])
#             if r == numsLen-1:
#                 return abs(nums[r] - nums[l-1]) - abs(nums[l]-nums[l-1])
            
#             return abs(nums[r + 1] - nums[l]) - abs(nums[r+1] - nums[r]) + abs(nums[r] - nums[l-1]) - abs(nums[l]-nums[l-1])
        
#         # print(findDelta(1,3))
#         oldSum = sum([abs(nums[i] - nums[i+1]) for i in range(numsLen-1)])
        
#         maxDelta = 0
#         for l in range(0, numsLen-1):
#             for r in range(l, numsLen):
#                 maxDelta = max(maxDelta, findDelta(l, r))
#         return oldSum + maxDelta

