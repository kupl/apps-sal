class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        from functools import lru_cache
        @lru_cache(maxsize = None)
        def bt(dieLeft, lastVal, lastConsecCount):
            if dieLeft == 0:
                return 1
            
            total = 0
            for i in range(0, 6):
                if i == lastVal and lastConsecCount == rollMax[i]:
                    continue
                else:
                    if i == lastVal:
                        newCount = lastConsecCount + 1
                        #print(lastVal, lastConsecCount)
                    else:
                        newCount = 1
                    
                    total += bt(dieLeft - 1, i, newCount)
                    if total > 10**9 + 7:
                        total = total % (10**9 + 7)
            return total
        
        return bt(n, None, None)
        
        

