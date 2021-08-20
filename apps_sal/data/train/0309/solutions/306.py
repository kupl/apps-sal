class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = dict()
        res = 0
        for j in range(len(A)):
            for i in range(j):
                diff = A[j] - A[i]
                if (diff, i) in memo:
                    memo[diff, j] = memo[diff, i] + 1
                else:
                    memo[diff, j] = 2
        max_val = max(memo.values())
        return max_val
