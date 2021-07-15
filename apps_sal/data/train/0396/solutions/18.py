class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        
        length = 1
        p10 = 10
        N = 1
        
        #any number not divisible by 2 or 5 will divide some number of the form 111...1
            #this requires a proof ofc
        
        if not K % 2:
            return -1
        
        if not K % 5:
            return -1
        
        while True:            
            if not N % K:
                return length            
            
            N += p10
            p10 *= 10
            length += 1
            

