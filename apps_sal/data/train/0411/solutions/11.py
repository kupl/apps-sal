class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + len(s) * [False]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
