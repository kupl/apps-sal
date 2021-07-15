class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        D = {}
        for x in A:
            D[x] = D.get(x, 0) + 1
            
        D = dict([x for x in sorted(list(D.items()), key =lambda x:x[0] )])
        
        for x in D:
            while D[x] > 0:
                D[x] -= 1
                if x <= 0:
                    pair_x = x / 2
                else:
                    pair_x = x * 2
                    
                if D.get(pair_x, 0) > 0:
                    D[pair_x] -= 1
                else:
                    return False
                
        return True
            

