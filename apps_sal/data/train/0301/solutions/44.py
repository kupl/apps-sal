class Solution:
    def maxUncrossedLines(self, A, B):
        # Optimization
        # commons = set(A).intersection(set(B)) # or commons = set(A) & set(B)
        #A = [x for x in A if x in commons]
        #B = [x for x in B if x in commons]

        N1, N2 = len(A), len(B)
        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]
        for i1, v1 in enumerate(A, start=1):
            for i2, v2 in enumerate(B, start=1):
                if v1 == v2:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
        return dp[N1][N2]


class Solution:
    def maxUncrossedLines(self, A, B):

        commons = set(A).intersection(set(B))  # or commons = set(A) & set(B)
        A = [x for x in A if x in commons]
        B = [x for x in B if x in commons]
        N1, N2 = len(A), len(B)
        dp = [0 for _ in range(N2 + 1)]
        for i1, v1 in enumerate(A, start=1):
            tmp = [0 for _ in range(N2 + 1)]
            for i2, v2 in enumerate(B, start=1):
                if v1 == v2:
                    tmp[i2] = dp[i2 - 1] + 1
                else:
                    tmp[i2] = max(dp[i2], tmp[i2 - 1])
            dp = tmp
        return dp[N2]
