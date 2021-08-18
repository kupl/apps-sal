class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            temp = [dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w))]
            dp[w] = max(temp)
        return max(dp.values())
