class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        a = len(A)
        b = len(B)
        memo = {}
        for i in range(a):
            for j in range(b):
                if A[i] == B[j]:
                    memo[(i, j)] = memo.get((i - 1, j - 1), 0) + 1
                else:
                    memo[(i, j)] = max(memo.get((i - 1, j), 0), memo.get((i, j - 1), 0))
        return max(memo.values())
