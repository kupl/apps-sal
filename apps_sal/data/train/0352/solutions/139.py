class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words.sort(key=lambda x: len(x))
        for w in words:
            maxLen = 0
            for i in range(len(w)):
                predecessor = w[:i] + w[i + 1:]
                maxLen = max(maxLen, dp.get(predecessor, 0) + 1)
            dp[w] = maxLen
        return max(dp.values())
