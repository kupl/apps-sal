class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        """
        DFS with memo
        """
        dp = {}

        def chainEndingAt(word):
            if word not in words:
                return 0
            if word not in dp:
                chain_len = 1
                for i in range(len(word)):
                    pred = word[:i] + word[i + 1:]
                    chain_len = max(chain_len, chainEndingAt(pred) + 1)
                dp[word] = chain_len
            return dp[word]
        ans = 0
        for word in words:
            ans = max(ans, chainEndingAt(word))
        return ans
        '\n        DP\n        dp function:\n        chain[word2] = max(chain[word1]+1 for all word1 if word1 is predecessor of word2)\n        '
