class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        """
        DFS with memo
        """
        words = set(words)
        dp = {}

        def chainEndingAt(word):
            if word not in words:
                return 0
            chain_len = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                chain_len = max(chain_len, chainEndingAt(pred) + 1)
            return chain_len
        ans = 0
        for word in words:
            ans = max(ans, chainEndingAt(word))
        return ans
        '\n        DP\n        dp function:\n        chain[word2] = max(chain[word1]+1 for all word1 if word1 is predecessor of word2)\n        '
