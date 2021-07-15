class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        
        if len(s) != len(t):
            return False
        
        d = defaultdict(int)
        
        for sc, tc in zip(s,t):
            
            diff = ( ord(tc) - ord(sc) ) % 26
            
            if diff == 0:
                continue
            
            if diff > k:
                return False
            
            d[diff] += 1
            
            if ((d[diff] - 1) * 26) + diff > k:
                return False
            
        
        return True
