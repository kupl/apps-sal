class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}
        def getPowerValue(x):
            if x in d:
                return d[x]
            steps = 0
            
            original = x
            while x != 1:
                if x%2:
                    x = 3*x+1
                else:
                    x /= 2
                    
                steps += 1
                
                if x in d:
                    steps += d[x]
                    break
        
            d[original] = steps
            return steps
        
        return sorted([x for x in range(lo, hi+1)], key=getPowerValue)[k-1]
