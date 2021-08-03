class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        A = sorted(A)
        # g[i][j] = 1 if A[i], A[j] are squareful
        g = [[0] * n for _ in range(n)]
        # dp[s][i]: number of ways to reach state s and ends with node i
        dp = [[0] * n for _ in range(1 << n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                r = int((A[i] + A[j]) ** 0.5)
                if r ** 2 == A[i] + A[j]:
                    g[i][j] = 1

        for i in range(n):
            if i == 0 or A[i] != A[i - 1]:
                dp[(1 << i)][i] = 1

        ans = 0
        for s in range(1 << n):
            for i in range(n):
                if not dp[s][i]:
                    continue
                for j in range(n):
                    if not g[i][j]:
                        continue
                    if s & (1 << j):
                        continue
                    if j > 0 and not (s & (1 << (j - 1))) and A[j - 1] == A[j]:
                        continue
                    dp[s | (1 << j)][j] += dp[s][i]

        for i in range(n):
            ans += dp[(1 << n) - 1][i]

        return ans
