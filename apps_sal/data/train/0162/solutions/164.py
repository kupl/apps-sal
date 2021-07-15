class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = [[None for j in range(len(text2))] for i in range(len(text1))]
        self.memo(text1,text2,0,0,cache)
        return cache[0][0]
    def memo(self,word1,word2,i,j,cache):
        if(i >= len(word1) or j >= len(word2)):
            return 0
        if(word1[i] == word2[j]):
            if(cache[i][j] is None):
                cache[i][j] = 1 + self.memo(word1,word2,i+1,j+1,cache)
            return cache[i][j]
        else:
            if(cache[i][j] is None):
                cache[i][j] = max(self.memo(word1,word2,i+1,j,cache), self.memo(word1,word2,i,j+1,cache))
            return cache[i][j]
        #TLE
        '''
        return self.recurse(text1,text2)
    def recurse(self, word1, word2):
        if(len(word1) == 0 or len(word2) == 0):
            return 0
        if(word1[0] == word2[0]):
            return 1 + self.recurse(word1[1:], word2[1:])
        else:
            return max(self.recurse(word1[1:],word2),self.recurse(word1,word2[1:]))'''
