class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        for i in range(len(A)):
            for j in range(i):
                interval = A[i] - A[j]
                if (interval, j) in memo:
                    memo[interval, i] = memo[interval, j] + 1
                else:
                    memo[interval, i] = 2
        return max(memo.values())
