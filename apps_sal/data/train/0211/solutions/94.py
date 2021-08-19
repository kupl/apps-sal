class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        dp = [[] for i in range(len(s))]
        dp[0].append([s[0]])
        for i in range(1, len(s)):
            for j in range(len(dp[i - 1])):
                comb = dp[i - 1][j]
                dp[i].append(comb[:-1] + [comb[-1] + s[i]])
                dp[i].append(comb + [s[i]])
        _max = 0
        for i in range(len(s)):
            for j in range(len(dp[i])):
                length = len(set(dp[i][j]))
                if length > _max:
                    _max = length
        return _max
