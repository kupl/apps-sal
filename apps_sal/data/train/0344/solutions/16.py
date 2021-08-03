class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        memo = [1 for _ in range(len(A[0]))]
        for i in range(len(A[0])):
            for j in range(i):
                if all(A[k][j] <= A[k][i] for k in range(len(A))):
                    memo[i] = max(memo[i], memo[j] + 1)
        return len(A[0]) - max(memo)
