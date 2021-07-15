class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        start = 0
        end = minSize
        counts = {}
        res = 0
        
        while start <= len(s)-minSize:
            item = s[start:end]
            counts[item] = counts.get(item, 0) + 1
            
            start += 1
            end += 1
            
        for i in counts:
            if self.countUnique(i) <= maxLetters:
                res = max(res, counts[i])
                  
        return res
        
    def countUnique(self, s):
        return len(set(s))
