class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s or len(s) < minSize:
            return 0
        gMax = -1
        while minSize <= maxSize:
            start = 0
            end = minSize - 1
            freqMap = {}
            lMax = 0
            while end < len(s):
                sub = s[start:end + 1]
                # print(sub, self.checkUnique(sub))
                if sub in freqMap or self.checkUnique(sub, maxLetters):
                    if sub not in freqMap:
                        freqMap[sub] = 1
                    else:
                        freqMap[sub] += 1
                    if freqMap[sub] > lMax:
                        lMax = freqMap[sub]
                start += 1
                end += 1
            # print(lMax, gMax, minSize)
            if lMax > gMax:
                gMax = lMax   
            minSize += 1
            
        return gMax
                        
                
                
    def checkUnique(self, string, maxLetters):
        sett = set(string)
        if len(sett) > maxLetters:
            return False
        else:
            return True
                
                

