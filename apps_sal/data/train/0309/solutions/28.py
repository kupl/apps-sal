class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = [{} for _ in range(len(A))] 
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                memo[i][diff] = 1 + memo[j].get(diff, 1)
        return max(d[diff] for d in memo for diff in d)
