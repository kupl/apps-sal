class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def custom_equal(word1, word2):
            if len(word2) == len(word1):
                return 0
            for i in range(len(word2)):
                if word2[0:i] + word2[i + 1:] == word1:
                    return 1
            return 0
        words.sort(key=lambda x: len(x))
        max_len = 1
        dp = [1 for _ in words]
        for i in range(1, len(words)):
            for j in range(i - 1, -1, -1):
                if len(words[j]) + 1 < len(words[i]):
                    break
                if custom_equal(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])
        return max_len
