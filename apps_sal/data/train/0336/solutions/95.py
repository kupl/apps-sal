class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        if len(s) != len(t) : return -1 
        
        elif sorted(s) == sorted(t) : return 0 
        
        # find the intersection 
        I = set(s).intersection(t) 
        
        # find frequency of I's in s and t and take minimum 
        freq_s = {}
        
        # find in s 
        for c in s:
            if c in I:
                freq_s[c] = freq_s.get(c,0) + 1 
                
        # find in t
        freq_t = {}
        for c in t:
            if c in I:
                freq_t[c] = freq_t.get(c, 0) + 1 
                
        
        # now take the minima of both 
        # take the sums of min freqs
        
        I_sum = 0 
        for c in list(freq_t.keys()):
            freq_t[c] = min ( freq_s[c], freq_t[c]) 
            
            I_sum += freq_t[c]
            
        return len(t) - I_sum 
            
            
            
        
                

