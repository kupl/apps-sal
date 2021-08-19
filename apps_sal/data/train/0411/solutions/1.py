class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i, -1, -1):
                if dp[j]:
                    word = s[j:i]
                    if word in wordDict:
                        dp[i] = True
                        break
        return dp[len(s)]
