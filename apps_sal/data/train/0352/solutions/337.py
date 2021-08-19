class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        DFS with memo
        '''
        words = set(words)
        dp = {}

        def chainEndingAt(word):
            if word not in words:
                return 0
            # if memo
            chain_len = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                chain_len = max(chain_len, chainEndingAt(pred) + 1)
            return chain_len

        ans = 0
        for word in words:
            ans = max(ans, chainEndingAt(word))
        return ans

        '''
        DP
        dp function:
        chain[word2] = max(chain[word1]+1 for all word1 if word1 is predecessor of word2)
        '''
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = 1
        #     for i in range(len(w)):
        #         dp[w] = max(dp[w], dp.get(w[:i] + w[i+1:],0) + 1)
        # return max(dp.values())
