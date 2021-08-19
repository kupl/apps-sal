from collections import defaultdict


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words = sorted(words, key=lambda x: len(x))
        dp = [1 for _ in range(len(words))]
        res = 1
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[j]) + 1 == len(words[i]) and self.isPred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    def isPred(self, word1, word2):
        if len(word1) + 1 != len(word2):
            return False
        p1 = 0
        p2 = 0
        degree = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
                continue
            else:
                degree += 1
                p2 += 1
        return degree < 2
