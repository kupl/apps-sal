class Solution:
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        l = jobDifficulty
        llen = len(l)
        if d>llen:
            return -1
        if llen==1:
            return l[0]
        dct = [[float('inf') for _ in range(d+1)] for _ in range(llen+1)]
 
            
            
        for i in range(1,llen+1):
            dct[i][1] = max(l[:i])
                
        
        for i in range(2, llen+1):
            for j in range(2,d+1):
                for k in range(1,i):
                    dct[i][j] = min(dct[i][j], dct[k][j-1]+max(l[k:i]))
                    
        return dct[llen][d]
                    
                    

