class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        
        length = 1
        p10 = 10
        N = 1
        
        #any number not divisible by 2 or 5 will divide some number of the form 111...1
            #proof by contradiction
            #let K be a number s.t. K is not divisible by 2 or 5 and does not divide a number of the form 111...1
            #now consider the sequence S = {1,11,111,...} Then by the pigeonhole principle there exists an x and y in
            #S such that y > x and y mod(K) = x mod(k) (since z mod(k) in {0,1,...,K-1} for all z). Then y - x mod(K) = 0.
            #So K divides y - x. By since both y - x are of the form 111...1, and y > x, y - x end in at least one zero.
            #This implies that K is divisible by 5 and 2, a contradiction.
        
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
            

