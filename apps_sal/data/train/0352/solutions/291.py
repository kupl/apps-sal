class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) <= 0:
            return 0
        
        words.sort(key=len)
        numberOfWords = len(words)
        longestLens = [1] * len(words)
        index = numberOfWords - 1
        
        while index >= 0:
            maxLen = 1
            index2 = index + 1
            while index2 < numberOfWords and len(words[index]) + 1 >= len(words[index2]):
                if self.isPredecessor(words[index], words[index2]):
                    if maxLen < longestLens[index2] + 1:
                        maxLen = longestLens[index2] + 1
                index2 += 1
            longestLens[index] = maxLen
            index -= 1
        
        maxLen = longestLens[0]
        for longestLen in longestLens:
            if maxLen < longestLen:
                maxLen = longestLen
        return maxLen
                    
    
    def isPredecessor(self, word1:str, word2:str)-> bool:
        if len(word2) - len(word1) != 1:
            return False
        for i, ch in enumerate(word2):
            newWord = word2[:i] + word2[i+1:]
            if newWord == word1:
                return True
        return False
    
        

