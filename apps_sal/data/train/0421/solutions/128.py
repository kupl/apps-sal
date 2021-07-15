from collections import defaultdict

class Solution:       
    def lastSubstring(self, s: str) -> str:
        max_char = None
        max_char_idx_all = set()
        max_string = None

        for i, c in enumerate(s):
            if max_char == None or c >= max_char:
                max_char = c
                new_string = s[i:]
                
                if max_string == None or new_string > max_string:
                    max_string = new_string            
        
        return max_string

