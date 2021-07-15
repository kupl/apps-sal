class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        def onediff(word1, word2):
            if len(word1) + 1 != len(word2) : return False
            for i in range(len(word2)):
                if word2[:i] + word2[i+1:] == word1 : 
                    return True
            return False
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(i):
                if onediff(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

