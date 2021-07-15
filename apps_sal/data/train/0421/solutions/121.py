from collections import defaultdict

class Solution:       
    def lastSubstring(self, s: str) -> str:
        all_strings = set()
        max_char = None
        char_to_idx = defaultdict(lambda: [])
        
        for i, c in enumerate(s):
            if max_char == None or c > max_char:
                max_char = c
            char_to_idx[c].append(i)
        
        max_string = None
        for start_idx in char_to_idx[max_char]:
            # for j in range(start_idx+1, len(s)+1):
            new_string = s[start_idx:]
            if max_string == None or new_string > max_string:
                max_string = new_string
        
        return max_string

