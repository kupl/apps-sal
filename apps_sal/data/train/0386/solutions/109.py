class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {}
        dp[1] = {}
        for c in ['a', 'e', 'i', 'o', 'u']:
            dp[1][c] = 1
        sources = {}
        sources['a'] = ['e','i','u']
        sources['e'] = ['a', 'i']
        sources['i'] = ['e', 'o']
        sources['o'] = ['i']
        sources['u'] = ['i', 'o']
        for i in range(2, n+1):
            dp[i] = {}
            for c in ['a', 'e', 'i', 'o', 'u']:
                dp[i][c] = sum(
                    dp[i-1][s] for s in sources[c]
                ) % 1000000007
        return sum(dp[n][c] for c in dp[n])  % 1000000007

