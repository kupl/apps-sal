from functools import lru_cache
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i):
            # return maximum length of positive from A
            
            # and maximum length of negative
            # starting from A[0]
            
            
            
            if i == len(nums)-1:
                if nums[i] > 0:
                    return 1,0
                elif nums[i] < 0:
                    return 0,1
                else:
                    return 0,0
                
            pos,neg = dp(i+1)
            
            
            if nums[i] == 0:
                # print(0,0,nums[i:])
                return 0, 0
            elif nums[i] > 0:
            
                a = pos + 1
                
                if neg == 0:
                    b = 0
                else:
                    b = neg + 1
                
                # print(a,b,nums[i:])
                
                return a, b
            else:
                
                a = 0
                b = 1
                
                if pos > 0:
                    b = max(b,pos + 1)
                
#                 if neg == 0:
#                     b = max(b,1)
                    
                if neg > 0:
                    a = max(a,neg + 1)
                    
                # print(a,b,nums[i:])
                
                return a, b
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dp(i)[0])
        
        return ans
            

