class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            # print()
            # print(w)
            temp = [dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w))]
            # print(temp)
            dp[w] = max(temp)
            # print(dp)
        return max(dp.values())

