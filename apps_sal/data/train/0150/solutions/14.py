from collections import Counter

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        
        c = Counter(A)
        d = Counter()
        
        keys = sorted(c.keys())
        
        d[keys[0]] = 0
        for i in range(1, len(keys)):
            d[keys[i]] = c[keys[i-1]] + d[keys[i-1]]
            
        lesscount, mx = 0, -float('inf')
        
        
        equal = 0
        
        for i in range(len(A)):
            # mx = max(mx, A[i])
            
            if A[i] < mx:
                lesscount += 1 
            elif A[i] == mx:
                equal += 1
            else:
                mx = A[i]
                lesscount += equal
                equal = 1
                

            # print(A[i], mx, lesscount, equal, d[mx])   
            if lesscount == d[mx]:
                return i + 1
            

