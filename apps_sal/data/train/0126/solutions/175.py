from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s or len(s) < minSize: return 0
        res = defaultdict(int)
        res[''] = 0
        temp = defaultdict(int)
    
        i = 0
        j = minSize-1

        for k in range(minSize):
            temp[s[k]] += 1
        
        if len(temp.keys()) <= maxLetters:
                res[s[i:j+1]] += 1
            
        while i < len(s)-minSize:
            temp[s[i]] -= 1
            i += 1
            j += 1
            temp[s[j]] += 1
            if len([l for l in temp if temp[l]]) <= maxLetters:
                res[s[i:j+1]] += 1
        
        return max(res.values())
