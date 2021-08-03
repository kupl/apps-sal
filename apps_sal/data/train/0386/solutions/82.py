class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9 + 7)

        # graph[0] = 'a' can come after 'e', 'i', 'u'
        # graph[1] = 'e' can come after 'a', 'i'
        # graph[2] = 'i' can come after 'e', 'o'
        # graph[3] = 'o' can come after 'i'
        # graph[4] = 'u' can come after 'i', 'o'
        graph = [[1, 2, 4], [0, 2], [1, 3], [2], [2, 3]]

        # dp[i] = number of ways that ends with letter i
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
