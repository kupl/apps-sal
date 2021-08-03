class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = [[None for i in range(len(B))] for i in range(len(A))]
        return self.uncrossRec(A, B, 0, 0, memo)

    def uncrossRec(self, A: List[int], B: List[int], i: int, j: int, memo):
        if j == len(B) or i == len(A):
            return 0
        if memo[i][j] != None:
            return memo[i][j]
        if A[i] == B[j]:
            memo[i][j] = 1 + self.uncrossRec(A, B, i + 1, j + 1, memo)
        else:
            x = self.uncrossRec(A, B, i, j + 1, memo)
            y = self.uncrossRec(A, B, i + 1, j, memo)
            memo[i][j] = max(x, y)
        return memo[i][j]
