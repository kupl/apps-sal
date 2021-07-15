class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        
        while len(nums)!=0:
            L=[]
            for i in range(len(nums)):
                if nums[i]==1:
                    c+=1
                elif nums[i]%2==1:
                    L.append(nums[i]//2)
                    c+=1
                elif nums[i]!=0 and nums[i]%2==0:
                    L.append(nums[i]//2)
            if len(L)!=0:
                c+=1
            nums=L
                        

                    
        return c                    

