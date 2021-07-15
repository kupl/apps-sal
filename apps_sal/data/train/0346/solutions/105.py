class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        return self.newConcept(nums,k) - self.newConcept(nums,k-1)
    
    
    
    
    
    def newConcept(self,nums,k):
        
        ans =0
        left = 0
        c = 0
        for i in range(len(nums)):
            if(nums[i]%2!=0):
                c+=1
            
           
                
            while(c>k):
                    
                    
                if(nums[left] % 2 != 0):
                    
                    c-=1
                        
                left+=1
                   
            ans+=i-left+1
        
        
        return ans

