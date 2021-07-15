class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = collections.defaultdict(int)
        for w in sorted(words, key = len):
            for i in range(len(w)):
                dp[w] = max(dp[w], 1 +  dp[w[:i] + w[i + 1:]])
        return max(dp.values())

