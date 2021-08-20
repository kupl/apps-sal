class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        DP = {}
        for i in range(1, len(A)):
            for j in range(len(A[:i])):
                d = A[i] - A[j]
                if (j, d) in DP:
                    DP[i, d] = DP[j, d] + 1
                else:
                    DP[i, d] = 2
        return max(DP.values())
