class Solution:
    def _is_pred(self, word1: str, word2: str) -> bool:
        if(not (len(word1) == len(word2)-1)):
            return False
        
        for c in word1:
            if c not in word2:
                return False
        
        return True
        
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1 for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                if(self._is_pred(words[j], words[i])):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return (max(dp))
