class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        
        for size in range(minSize, maxSize+1):
            for i in range(len(s) - size + 1):
                sub_str = s[i:i+size]
                
                if len(set(sub_str)) > maxLetters: continue
                
                if sub_str in freq:
                    freq[sub_str] += 1
                else:
                    freq[sub_str] = 1
                
        max_freq = 0
        
        for sub_str, cnt in list(freq.items()):
            max_freq = max(max_freq, cnt)
            
        return max_freq

