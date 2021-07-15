class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        
        ######Approach 1 log (n^2)
#         nums.sort()
#         if not nums:
#             return 0
        
#         total=0
#         print(nums)
#         for i in range(len(nums)):
#             for j in range(len(nums)-1,i-1,-1):
#                 if nums[i]+nums[j]<=target:
#                     total+=pow(2, j-i, 10**9 + 7)
#                     break
#         return total % (10**9 + 7)

##########Approach 2 log(n) 
        low=0
        high=len(nums)-1
        nums.sort()
        if not nums:
            return 0
        total=0
        while low<=high:
            if nums[low]+nums[high]<=target:
                total+=pow(2, high-low, 10**9 + 7)
                low+=1
            else:
                high-=1
        return total %(10**9 + 7)
                
            

