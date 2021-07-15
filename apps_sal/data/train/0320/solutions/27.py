class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        twoes = 0
        
        for i in nums:
            c = 0
            while i:
                if i%2:
                    i-=1
                    ones+=1
                else:
                    i //=2
                    c+=1
            twoes = max(twoes,c)
            
        return ones+twoes
                
            

