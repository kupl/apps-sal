class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        res = []
        
        for i in range(lo,hi+1):
            sol = [i]
            
            count = 0
            
            while i != 1:
                if i %2 == 0:
                    i//=2
                else: 
                    i = 3*i+1
                count += 1
            
            sol = [count, sol[0]]
            res.append(sol)
        
        result = sorted(res)
        
        
        ff = [x[1] for x in result]
        return ff[k-1]
