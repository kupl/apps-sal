class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones=0
        maxlen=0
        binlen=0
        for num in nums:
            binlen=0
            while num!=0:
                if num%2!=0:
                    ones+=1
                    num-=1
                    
                if num!=0:
                    num//=2
                    binlen+=1
            maxlen=max(maxlen,binlen)
            
        return maxlen+ones
        
        
#         op=0
#         sum1=sum(nums)
#         while sum1!=0:
#             for i in range(len(nums)):
#                 if nums[i]%2!=0:
#                     nums[i]-=1
#                     sum1-=1
#                     op+=1
                    
#             if sum1==0:
#                 return op
            
#             for i in range(len(nums)):
#                 nums[i]//=2
#             op+=1
#             sum1/=2
            
#         return op

