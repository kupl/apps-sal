from collections import Counter


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def check_predecessor(s1, s2):
            if len(s1) != len(s2) - 1:
                return False
            for i in range(len(s2)):
                if s1 == (s2[:i] + s2[i + 1:]):
                    return True
            return False

        dp = [1] * len(words)
        res = 1

        for i in range(len(words)):
            for j in range(i):
                if check_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        return res
