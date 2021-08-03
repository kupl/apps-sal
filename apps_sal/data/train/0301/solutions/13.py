class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        from bisect import bisect

        a, b = len(A), len(B)
        indA = defaultdict(list)
        indB = defaultdict(list)
        for i, num in enumerate(A):
            indA[num].append(i)
        for i, num in enumerate(B):
            indB[num].append(i)

        dp = {}
        for i, num1 in enumerate(A):
            for j, num2 in enumerate(B):
                if num1 == num2:
                    dp[(i, j)] = 1 + (dp[(i - 1, j - 1)] if min(i, j) > 0 else 0)
                else:
                    ii = bisect(indB[num1], j) if num1 in indB else 0
                    jj = bisect(indA[num2], i) if num2 in indA else 0
                    iii = -1 if ii == 0 else indB[num1][ii - 1]
                    jjj = -1 if jj == 0 else indA[num2][jj - 1]
                    dp[i, j] = dp[i - 1, j - 1] if min(i, j) > 0 else 0
                    if iii >= 0:
                        dp[i, j] = max(dp[i, j], 1 + dp[i - 1, iii - 1] if min(i, iii) > 0 else 1)
                    if jjj >= 0:
                        dp[i, j] = max(dp[i, j], 1 + dp[jjj - 1, j - 1] if min(j, jjj) > 0 else 1)

        return dp[a - 1, b - 1]
