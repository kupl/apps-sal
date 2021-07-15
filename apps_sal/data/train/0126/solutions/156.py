class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s:
            return 0
        
        n = len(s)
        substring_count = defaultdict(int)
        
        memo_char = defaultdict(int)
        reader = 0
        writer = 0
        
        while reader < len(s):
            ch = s[reader]
            memo_char[ch] += 1
            window_len = reader - writer +1
            
            while len(memo_char) > maxLetters or window_len > minSize:
                wch = s[writer]
                memo_char[wch] -= 1
                
                if memo_char[wch] == 0:
                    del memo_char[wch]
                
                writer += 1
                window_len = reader - writer +1
            if window_len >= minSize and window_len <= maxSize:
                substring_count[tuple(s[writer:reader+1])] += 1
                #print (s[writer:reader+1], substring_count, window_len)
            reader += 1
            
        if not substring_count:
            return 0
        
        return max(substring_count.values())
        
        

