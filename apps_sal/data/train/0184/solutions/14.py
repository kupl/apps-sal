from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(text) == 0:
            return 0
        
        seen = set()
        max_count = 0
        i = j = 0
        window = Counter()
        maxes = Counter()
        
        while j < len(text):
            if len(window) > 2 or (len(window) == 2 and min(window.values()) != 1):
                maxes[text[i]] = max(maxes[text[i]], window[text[i]])
                window[text[i]] -= 1
                if window[text[i]] == 0:
                    del window[text[i]]
                i += 1
            else:
                inc = 0
                cur_char = text[j]
                window[cur_char] += 1
                
                if cur_char in maxes:
                    max_count = max(max_count, maxes[cur_char] + 1)
                    inc = 1
                    
                max_count = max(max_count, window[cur_char] + inc)
                
                j += 1

        return max_count
                
                
        

