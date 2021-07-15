from collections import defaultdict

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        MOD = 10**9 + 7
        
        dice = defaultdict(int)
        mem = {}
        
        def helper(i, predie, count):
            if i == n:
                return 1
            
            if (i,predie,count) in mem:
                return mem[(i,predie,count)]
            
            
            out = 0
            for die in range(6):
                if die == predie and count == rollMax[die]:
                    continue
                v, c = die, 1
                if die == predie:
                    c = count + 1
                out += helper(i+1, v, c) 
                    
            mem[(i,predie,count)] = out % MOD
                    
            return mem[(i,predie,count)]
        
        
        
        return helper(0, -1, -1)
            
            
            
            
            

