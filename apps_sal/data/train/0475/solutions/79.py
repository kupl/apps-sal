class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        #get the array of sum of all continuous subarrays
        
        res = []
        
        
        for i in range(len(nums)):
            
            temp = 0
            
            for j in range(i,len(nums)):
                
                temp+=nums[j]
                res.append(temp)
                
                
        res.sort()
        
        ans = sum(res[left-1:right])
        
        return ans % (10**9+7)
        

