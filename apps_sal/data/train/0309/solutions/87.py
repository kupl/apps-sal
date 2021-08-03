class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = dict()
        n = len(A)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                d = A[j] - A[i]
                if (j, d) in memo:
                    memo[(i, d)] = memo[(j, d)] + 1
                else:
                    memo[(i, d)] = 2
        return max(memo.values())
