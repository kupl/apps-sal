class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [-1] + A
        B = [-1] + B
        (lenA, lenB) = (len(A), len(B))
        dp = [[0] * lenA for _ in range(lenB)]
        for y in range(1, lenB):
            for x in range(1, lenA):
                if A[x] == B[y]:
                    dp[y][x] = dp[y - 1][x - 1] + 1
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
        return dp[-1][-1]
