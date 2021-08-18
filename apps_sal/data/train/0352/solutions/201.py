class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [0 for i in range(len(words))]
        ans = 0
        words = sorted(words, key=lambda x: len(x))
        for i in range(len(words)):
            for j in range(i):
                if self.prev(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])

        return ans + 1

    def prev(self, word_1, word_2):
        len_1, len_2 = len(word_1), len(word_2)
        if len_1 + 1 != len_2:
            return False

        i = j = 0
        while i < len_1 and j < len_2:
            if word_1[i] == word_2[j]:
                i += 1
            j += 1
        if i == len_1:
            return True
        else:
            return False
