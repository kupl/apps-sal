class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)

        memo = [(1 + 2 * 500) * [1] for _ in range(1 + len(A))]

        res = 2

        for i in range(len(A) - 2, -1, -1):
            Ai = A[i] - 500
            mi = memo[i]

            for j in range(i + 1, len(A)):
                diff = A[j] - Ai
                mi[diff] = max(mi[diff], memo[j][diff] + 1)

            res = max(res, max(mi))

        return res
