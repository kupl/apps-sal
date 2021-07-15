class Solution:
    def minOperations(self, n: int) -> int:
        # tot=0
        # quant = 0
        # for i in range(n):
        #     quant = abs(n - (2*i+1))
        #     if( quant> 0):
        #         tot +=  quant
        
        return sum([abs(n-2*i-1)  for i in range(n) if abs(n-2*i-1) > 0]) // (2)
            
            
            
        
            
        
            
            

