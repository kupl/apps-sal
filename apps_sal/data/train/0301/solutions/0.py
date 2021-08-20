from collections import defaultdict


class Solution:

    def maxUncrossedLines(self, A, B):
        (N1, N2) = (len(A), len(B))
        dp = [[0 for _ in range(N2 + 1)] for _ in range(N1 + 1)]
        for (i1, v1) in enumerate(A, start=1):
            for (i2, v2) in enumerate(B, start=1):
                if v1 == v2:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
        return dp[N1][N2]


class Solution:

    def maxUncrossedLines(self, A, B):
        commons = set(A).intersection(set(B))
        A = [x for x in A if x in commons]
        B = [x for x in B if x in commons]
        (N1, N2) = (len(A), len(B))
        dp = [0 for _ in range(N2 + 1)]
        for (i1, v1) in enumerate(A, start=1):
            tmp = [0 for _ in range(N2 + 1)]
            for (i2, v2) in enumerate(B, start=1):
                if v1 == v2:
                    tmp[i2] = dp[i2 - 1] + 1
                else:
                    tmp[i2] = max(dp[i2], tmp[i2 - 1])
            dp = tmp
        return dp[N2]


class Solution:

    def maxUncrossedLines(self, A, B):
        f = defaultdict(list)
        for (idx, val) in enumerate(B):
            f[val].insert(0, idx)
        dp = [0] * len(B)
        for val in A:
            for j in f[val]:
                dp[j] = max(dp[j], max(dp[:j], default=0) + 1)
        return max(dp)
