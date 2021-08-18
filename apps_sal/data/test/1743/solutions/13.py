

class Solution():
    def max_radiance(n, a, b, c):
        dp = [[0 for i in range(2)] for j in range(n + 1)]
        dp[n - 1][0] = a[n - 1]
        dp[n - 1][1] = b[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i][0] = max(a[i] + dp[i + 1][1], b[i] + dp[i + 1][0])
            dp[i][1] = max(b[i] + dp[i + 1][1], c[i] + dp[i + 1][0])

        return dp[0][0]


n = int(input())

a = list(map(int, input().strip(' ').split(' ')))
b = list(map(int, input().strip(' ').split(' ')))
c = list(map(int, input().strip(' ').split(' ')))

print(Solution.max_radiance(n, a, b, c))
