class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odd = 0
        counts = defaultdict(lambda: 0)
        
        for c in s:
            counts[c] += 1
            if (counts[c]%2 == 0): 
                odd -= 1
            else:
                 odd += 1
        
        if (odd > k or k>len(s)): return False
        
        return True
