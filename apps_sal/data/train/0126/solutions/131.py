class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        count = 0
        diff = maxSize-minSize
        hashM = {}
        maxC = float('-inf')
        
        for r in range(len(s)-minSize+1):
            
            for i in range(diff+1):
                
                if r + minSize + i <= len(s):
                    if len(set(s[r:r+minSize+i])) <= maxLetters:

                        hashM[s[r:r+minSize+i]] = hashM.get(s[r:r+minSize+i], 0) + 1
                        maxC = max(maxC, hashM[s[r:r+minSize+i]])
                        
        return(maxC if maxC != float('-inf') else 0)

