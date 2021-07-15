from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        one = self.atMostK(A, K)
        two = self.atMostK(A, K-1)
        print((one, two))
        return one-two
        
    def atMostK(self,nums, k):
        mapping = defaultdict(int)
        ans = 0 
        left = 0 
        for right in range(len(nums)):
            mapping[nums[right]]+=1
            if mapping[nums[right]] == 1:
                k-=1
                
            
            while k <0:
                mapping[nums[left]] -=1
                if mapping[nums[left]] == 0:
                    k+=1
                left+=1
                
            ans+=right-left+1
            
        return ans 
        
        
                
                
            
                
        
        

