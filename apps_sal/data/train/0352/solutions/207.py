class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words,key = len):
            for i in range(len(word)):
                # print(word[:i])
                if word[:i] + word[i+1:] in words:
                    dp[word] = dp.get(word[:i]+word[i+1:],1) + 1
                    res = max(res,dp[word])
        return res
