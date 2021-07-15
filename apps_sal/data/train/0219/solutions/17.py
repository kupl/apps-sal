class Solution:
    def longestWPI(self, hours):
        
        res = score = 0
        seen = {}
        
        for i, h in enumerate(hours):
            print((i,h))
            
            if h > 8: score += 1
            else: score -= 1
                
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res
    
    
#tiring_count = 1, not_tiring_count = 0, max_length = 1
#tiring_count = 2, not_tiring_count = 0, max_length = 2
#tiring_count = 2, not_tiring_count = 1, max_length = 3
#tiring_count = 2, not_tiring_count = 2, tiring_count = 0
#tiring_count = 0, nt = 3
#nt = 4
#tiring count += 1
                    

