class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # dp[i][j] min num of changes to divide j+1 subs in s[: i+1]
        # dp[i][j] = min([dp[i-m][j-1] + cost(i-m, j) for m in range(0, i)]
        n = len(s)
        dp = [[0 for j in range(k)] for i in range(n)]
        memo = {}
        # define the cost to make s[i: j+1] padindrome

        def cost(i, j):
            if memo.get((i, j)):
                return memo[(i, j)]
            c = 0
            while i < j:
                if s[i] != s[j]:
                    c += 1
                i += 1
                j -= 1
            memo[(i, j)] = c
            return c

        # we need to determine the maximum length of Palindrome centered at s[i]
        for i in range(n):
            for j in range(k):
                if j > i:
                    break
                if j == 0:
                    dp[i][j] = cost(0, i)
                else:
                    dp[i][j] = min([dp[m][j - 1] + cost(m + 1, i) for m in range(i) if j - 1 <= m])
        return dp[n - 1][k - 1]
