class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mul = [0 for i in range(len(nums))] #for each number of increment by 1 needed
        res = 0
        for i in range(len(nums)):
            while nums[i]!=0:
                if nums[i]%2 ==1:
                    res +=1
                    nums[i]-=1
                else:
                    mul[i]+=1
                    nums[i]//=2
            
        return res + max(mul)
                
           
            

