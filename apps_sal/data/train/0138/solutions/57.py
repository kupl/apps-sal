class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pos[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
                neg[i] = 1 + pos[i-1]
            elif nums[i] > 0:
                pos[i] = 1 + pos[i-1]
                neg[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
            else:
                pos[i] = 0
                neg[i] = 0
        return max(pos)
        
'''
pos[i] = max length subarray ending at i whose product is positive
neg[i] = max length subarray ending at i whose product is negative


pos[i] = (
    1 + pos[i-1], if nums[i] > 0
    1 + neg[i-1] elif nums[i] < 0
    0            else
)

neg[i] = (
    1 + neg[i-1], if nums[i] > 0
    1 + pos[i-1], elif nums[i] < 0
    0             else
)

A = [-1,-2,-3,0,1]
p = [0,  2, 2,]
n = [1,  1, 3]



[0,1,-2,-3,-4]

[0,1,0,3,2]
[0,0,2,1,]




'''
