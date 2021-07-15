from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)
        d = defaultdict(int)
        max_freq = 0
        for idx, a in enumerate(s):
            count[a] += 1
            if idx > minSize - 1:
                last = s[idx - minSize]
                count[last] -= 1
                if count[last] == 0:
                    del count[last]
            
            if idx >= minSize - 1:
                if len(count) <= maxLetters:
                    d[s[idx-minSize+1: idx+1]] += 1
                    max_freq = max(max_freq, d[s[idx-minSize+1: idx+1]])
        
        return max_freq
                
            

