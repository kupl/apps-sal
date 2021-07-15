class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {}
        for v in ('a', 'e', 'i', 'o', 'u'):
            dp[v] = [1] + [0] * (n - 1)
        for i in range(1, n):
            dp['a'][i] = sum(dp[v][i-1] for v in ('e', 'i', 'u'))
            dp['e'][i] = sum(dp[v][i-1] for v in ('a', 'i'))
            dp['i'][i] = sum(dp[v][i-1] for v in ('e', 'o'))
            dp['o'][i] = dp['i'][i-1]
            dp['u'][i] = sum(dp[v][i-1] for v in ('i', 'o'))
        return sum(row[-1] for row in dp.values()) % (10 ** 9 + 7)
