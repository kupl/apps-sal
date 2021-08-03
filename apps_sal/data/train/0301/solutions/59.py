class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * len(A) for _ in range(len(B))]

        for i in range(len(memo)):
            for j in range(len(memo[0])):

                if B[i] == A[j]:
                    memo[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        memo[i][j] += memo[i - 1][j - 1]
                sub_a = 0
                if j - 1 >= 0:
                    sub_a = memo[i][j - 1]
                sub_b = 0
                if i - 1 >= 0:
                    sub_b = memo[i - 1][j]
                memo[i][j] = max(memo[i][j], sub_a, sub_b)
        return memo[-1][-1]
