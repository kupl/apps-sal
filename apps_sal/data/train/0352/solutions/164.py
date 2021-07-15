class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = [1] * n
        words.sort(key=len)
        for i in range(1, n):
            for j in range(i):
                if self.is_predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def is_predecessor(self, word1, word2):
        if len(word1) - len(word2) != 1:
            return False
        i1 = 0
        i2 = 0
        diff = 0
        while i1 < len(word1) and i2 < len(word2):
            if word1[i1] == word2[i2]:
                i1 += 1
                i2 += 1
            else:
                i1 += 1
                diff += 1
                if diff > 1:
                    return False
        return True

