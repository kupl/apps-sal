class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for x,y in zip(s,t):
            change = 0
            if ord(y) - ord(x) > 0:
                change = ord(y) - ord(x)
            elif ord(y) - ord(x) < 0:
                change = (ord(y) - ord(x)) + 26
                
            if change == 0:
                continue
                
            if change not in count:
                count[change] = 1
            else:
                count[change] += 1
            
            
            if (count[change] - 1) * 26 + change > k:
                return False
        
        
                    
        return True
        

