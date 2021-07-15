class Solution:
    def dist(self, a,b):
        return (ord(b)-ord(a)) % 26
    
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): 
            return False
        seen = {}
        for x, y in zip(s, t):
            if x == y: 
                continue
            d = self.dist(x,y)            
            if d  > k: 
                return False
            if d not in seen: 
                seen[d] = d
            else:
                last = seen[d]
                if last + 26 > k: 
                    return False
                seen[d] = last + 26
        return True

