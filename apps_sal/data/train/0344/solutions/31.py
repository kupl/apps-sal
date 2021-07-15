class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        memo = [1] * n
        for i in range(n):
            for j in range(i):
                for k in range(m):
                    if A[k][j] > A[k][i]:
                        break
                else:
                    memo[i] = max(memo[i], memo[j] + 1)
        return n - max(memo)
