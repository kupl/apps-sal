class Solution:
    def carFleet(self, target: int, P: List[int], S: List[int]) -> int:
        n = len(P)
        
        l = []
        for i in range(n):
            l.append((P[i],S[i]))
        
        l.sort(reverse=True)
        
        c = 0
        pt = -1
        for i,j in l:
            ct = (target - i) / j
            if ct > pt:
                c += 1
                pt = ct
                
        return c
