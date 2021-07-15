class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        N = len(words)
        self.longest = [None]*N
        max_len = 1
        for i in range(N):
            max_len = max(max_len, self.__findLongestAfter(words, i))
            
        return max_len
                                    
                
    def __isPredecessor(self, w1, w2):
        if len(w2) != len(w1)+1:
            return False
        
        for i in range(len(w2)):
            if (w2[:i]+w2[i+1:]) == w1:
                return True
        return False
    
    def __findLongestAfter(self, words: List[str], i:int) -> int:
        if self.longest[i] is not None:
            return self.longest[i]
        
        max_len = 1
        for j in range(i+1, len(words)):
            if self.__isPredecessor(words[i], words[j]):
                max_len = max(max_len, self.__findLongestAfter(words, j)+1)
                
        self.longest[i] = max_len
        return max_len
