class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        
        n2p = []
        p2n = {}
        for x in range(n+1): 
            n2p.append(x**2)
            p2n[x**2] = x
        
        #print(n2p)
        #print(p2n)
        
        @lru_cache(None)
        def recur(rem):
            if rem == 0: return False
            if round(math.sqrt(rem)) ** 2 == rem: return True
            
            
            #print(\"rem\", rem)
            max_rm_val = math.floor(math.sqrt(rem))**2
            #print(\"val\", max_rm_val)
            max_rm_ind = p2n[max_rm_val]
            
            for ind in range(max_rm_ind, 0, -1):
                
                # hope that at least one next call returns False
                if not recur(rem - n2p[ind]): return True
            
            return False
        
        return recur(n)
