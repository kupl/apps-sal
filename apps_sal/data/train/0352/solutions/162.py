class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: (len(word)))
        lengths = [1] * len(words)
        for i in range(len(words)):
            for j in range(i):
                if self.checkifSuccessor(words[j],words[i]):
                    lengths[i] = max(lengths[i], lengths[j] + 1)
        return max(lengths)
                    
                
    def checkifSuccessor(self, word1, word2):
        if len(word1) + 1 !=  len(word2):
            return False
        else:
            indexOfword1 = 0
            differentReached = False
            for a in range(len(word2)):
                if indexOfword1 == len(word1):
                    break
                if word2[a] == word1[indexOfword1]:
                    indexOfword1 += 1
                else:
                    if differentReached == True:
                        return False
                    else:
                        differentReached = True
            return True
            
                    

