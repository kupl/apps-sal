class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        # maxSequence = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                # if val > maxSequence:
                #     maxSequence = val
        return max(v1 for dic in dp for v1 in dic.values())
