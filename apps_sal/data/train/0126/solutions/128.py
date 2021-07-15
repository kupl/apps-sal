class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        validStrings = {}
        for currSize in range(minSize, maxSize+1):
            self.getValidString(currSize, s, maxLetters, validStrings)
        return self.getMaxCount(validStrings)
        
    def getValidString(self,currSize, s, maxLetters, validStrings):
        left = 0
        right = 0
        currWindow = {}
        uniqueCounts = 0
        for right in range(currSize):
            uniqueCounts = self.insert(s[right],currWindow, uniqueCounts)
        self.insertValidString(uniqueCounts,maxLetters, left, right, s, validStrings )
        while right < len(s)-1:
            uniqueCounts = self.insert(s[right+1],currWindow, uniqueCounts)
            uniqueCounts = self.remove(s[left],currWindow, uniqueCounts)
            left += 1
            right += 1
            self.insertValidString(uniqueCounts,maxLetters, left, right, s, validStrings )
            
    def insert(self,char,currWindow, uniqueCounts):
        if char not in currWindow:
            currWindow[char] = 1
            uniqueCounts += 1
        else:
            currWindow[char] += 1
        return uniqueCounts
    
    def remove(self,char,currWindow, uniqueCounts):
        currWindow[char] -= 1
        if currWindow[char] == 0:
            del currWindow[char]
            uniqueCounts -= 1
        return uniqueCounts
    
    def getMaxCount(self,validStrings):
        maxCount = 0
        for string in validStrings:
            if validStrings[string] > maxCount:
                maxCount = validStrings[string]
        return maxCount
    
    
    def insertValidString(self,uniqueCounts,maxLetters, left, right, s, validStrings ):
        if uniqueCounts <= maxLetters:
            currWord = s[left:right+1]
            if currWord not in validStrings:
                validStrings[currWord] = 1
            else:
                validStrings[currWord] += 1
