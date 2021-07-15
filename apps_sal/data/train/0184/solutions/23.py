from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if not text:
            return 0
        
        cnt = Counter(list(text))
        output = 0
        
        for c, n in cnt.items():
            val = 0
            holder = 0
            
            for i, t in enumerate(text):
                if t == c:
                    val += 1
                else:
                    holder = val
                    val = 0
                
                if val + holder < n:
                    op = val + holder + 1
                else:
                    op = val + holder
                    
                output = max(output, op)
        
        return output
