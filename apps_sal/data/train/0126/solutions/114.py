class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        occurence = {}
        
        for i in range(len(s)):
            for j in range(minSize,maxSize+1):
                if i+j > len(s): 
                    break
                if len(set(s[i:i+j])) <= maxLetters:
                    if s[i:i+j] not in occurence:
                        occurence[s[i:i+j]] = 0
                    occurence[s[i:i+j]]+=1
        # print(occurence)
        if len(occurence) == 0:
            return 0
        return max(occurence.values())
