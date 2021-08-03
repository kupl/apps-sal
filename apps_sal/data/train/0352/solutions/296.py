
class Solution:
    def longestStrChain(self, words) -> int:
        len_words = len(words)
        dp = [1] * len_words
        res = 0
        words.sort(key=len)
        for i in range(len_words):
            max_value = 0
            for j in range(i):
                if not self.checkChild(words[j], words[i]):
                    continue
                max_value = max(max_value, dp[j])
            dp[i] = max_value + 1
            res = max(res, dp[i])
        return res

    def checkChild(self, word1, word2):
        if len(word1) != len(word2) - 1:
            return False
        from collections import Counter
        counter1 = Counter(word1)
        count = 0
        for ch in word2:
            if ch in counter1:
                counter1[ch] -= 1
                if counter1[ch] == 0:
                    counter1.pop(ch)
            else:
                count += 1
            if count > 1:
                return False
        return True
