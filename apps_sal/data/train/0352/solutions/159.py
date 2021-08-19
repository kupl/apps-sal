from collections import defaultdict


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=lambda x: len(x))
        for w in words:
            maxLen = 0
            for i in range(len(w)):
                predecessor = w[:i] + w[i + 1:]
                maxLen = max(maxLen, dp[predecessor] + 1)
            dp[w] = maxLen
        return max(dp.values())
