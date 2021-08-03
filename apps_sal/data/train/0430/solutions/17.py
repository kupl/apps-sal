class Solution:
    def distinctSubseqII(self, s: str) -> int:
        isvisited = [-1] * len(s)
        d = dict()
        for i in range(len(s)):
            if s[i] in d:
                isvisited[i] = d[s[i]]
            d[s[i]] = i
        dp = [1] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            if isvisited[i - 1] == -1:
                dp[i] = dp[i - 1] * 2
            else:
                dp[i] = 2 * dp[i - 1] - dp[isvisited[i - 1]]
        return (dp[-1] - 1) % 1000000007
