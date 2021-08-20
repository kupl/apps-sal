class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if (i, A[j] - A[i]) in memo:
                    memo[j, A[j] - A[i]] = memo[i, A[j] - A[i]] + 1
                else:
                    memo[j, A[j] - A[i]] = 2
        return max(memo.values())
