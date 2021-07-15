from itertools import combinations
from math import ceil

class Solution:
    
    def maxUniqueSplit(self, s: str) -> int:
        
        l, r = 1, len(s)
        
        def check(n):
            
            if n == 1: return True
            
            pos = [i + 1 for i in range(len(s) - 1)]
            
            for dividers in combinations(pos, n - 1):
                
                i = 0
                words = set()
                flag = 0
                for p in dividers:
                    if s[i: p] in words:
                        flag = 1
                        break
                    words.add(s[i: p])
                    i = p
                    
                if not flag and s[i: len(s)] not in words: 
                    return True
                          
            return False 
        
        while l < r:
            
            mid = l + (r - l) // 2 + 1
            
            if check(mid):
                l = mid
            else:
                r = mid - 1
        
        return r
        
        
        
        

