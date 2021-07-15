class Solution:
    def __init__(self):
        self.cache = collections.defaultdict(int)
    
    def longestEndWith(self, word, words):
        if word in self.cache:
            return self.cache[word]
        if len(word) == 1:
            self.cache[word] = 1
            return 1
        else:
            for i in range(len(word)):
                s = word[:i] + word[i+1:]
                if s in words:
                    self.cache[word] = max(self.cache[word], self.longestEndWith(s, words))
            self.cache[word] += 1
            return self.cache[word]
        
    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        
        for word in words:
            ans = max(ans, self.longestEndWith(word, words))
        
        return ans
