class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        shifts = [0 for x in range(1, 27)]
        
        for i in range(len(s)):
            if t[i] == s[i]:
                continue
            diff = (ord(t[i]) - ord(s[i])) % 26
            
            if ((shifts[diff]) * 26 + diff) > k:
                return False
            shifts[diff] += 1
        
        return True
