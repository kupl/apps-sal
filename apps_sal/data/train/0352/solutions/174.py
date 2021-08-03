class Solution:
    def longer_by_one(self, word1, word2):
        if len(word2) - len(word1) != 1:
            return False
        j = 0
        count = 0
        for i in range(len(word2)):
            if i < len(word2) and j < len(word1) and word2[i] != word1[j]:
                count += 1
                if count > 1:
                    return False
                continue
            j += 1

        if i == len(word2) - 1 and j == len(word1) and count == 1:
            return True
        elif i == len(word2) - 1 and j >= len(word1) and count == 0:
            return True
        else:
            return False

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1] * len(words)
        words = sorted(words, key=lambda x: len(x))
        for i in range(1, len(words)):
            for j in range(0, i):
                if self.longer_by_one(words[j], words[i]) == True:
                    dp[i] = max(dp[i], dp[j] + 1)
        for i in range(len(dp)):
            print((words[i], dp[i]))
        return max(dp)
