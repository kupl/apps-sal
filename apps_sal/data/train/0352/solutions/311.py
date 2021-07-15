class Solution:
    def longestStrChain(self, words: List[str]) -> int:
#         words.sort(key=len)
        
#         dp = {}
#         ans = 1
        
#         for word in words:
#             dp[word] = 1
#             for i in range(len(word)):
#                 cand = word[:i] + word[i+1:]
#                 if cand in dp:
#                     dp[word] = max(dp[word], dp[cand] + 1)
#                     ans = max(ans, dp[word])    
#         return ans
               
        if not words:
            return 0
        
        self.memo = {}
        self.ans = 1
        self.words = set(words)
        for word in self.words:
            self.dfs(word, 1)
        return self.ans
        
    def dfs(self, word, count):   
        if len(word) == 1:
            self.memo[word] = 1
            return 1
                
        self.memo[word] = 1
        for i in range(len(word)):
            nxt = word[:i] + word[i+1:]
            if nxt in self.words:
                self.memo[word] = max(self.memo[word], 1+self.dfs(nxt, count + 1))
                self.ans = max(self.ans, self.memo[word])
        return self.memo[word]
