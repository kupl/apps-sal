class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dict = {}
        left, right = 0, minSize
        while left < len(s):
            while right - left <= maxSize and right <= len(s):
                sub = s[left:right]
                if sub in dict:
                    dict[sub] += 1
                elif self.isUniqueAmount(sub, maxLetters):
                    dict[sub] = 1

                right += 1
            
            left += 1
            right = left + minSize
        
        retValue = 0
        for k, v in list(dict.items()):
            retValue = max(retValue, v)
        
        return retValue
    
    def isUniqueAmount(self, s: str, maxLetters: int) -> bool:
        return len(set(s)) <= maxLetters 

