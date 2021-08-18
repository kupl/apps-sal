class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9 + 7)

        graph = [[1, 2, 4], [0, 2], [1, 3], [2], [2, 3]]

        dp = [1] * 5

        for i in range(n - 1):
            copy = dp[:]
            for j in range(5):
                dp[j] = 0
                for k in graph[j]:
                    dp[j] += copy[k]
                    dp[j] %= mod

        ans = 0

        for cnt in dp:
            ans += cnt
            ans %= mod

        return ans
