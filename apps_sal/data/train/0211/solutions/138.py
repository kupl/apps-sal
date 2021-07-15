#Bit Mask: use bit 1 as fence. chars between two bit 1's form a substring
#Possible choices: 2 ** N (0 ~ 2 **N - 1)
#Note: that last bit/fence does not matter so we can save computations by half
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N, res = len(s), 0
        
        for i in range(2 ** (N - 1)):
            start, seen = 0, set()
            for j in range(N):
                #test to see if j-th bit is 1
                if (i + (1 << N - 1)) & (1 << j):
                    seen.add(s[start : j + 1])
                    start = j + 1
            
            res = max(res, len(seen))
        
        return res
                
        
        

