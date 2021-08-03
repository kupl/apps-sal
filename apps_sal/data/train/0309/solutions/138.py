class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[index][diff] := the longest arithmetic subsequence in A[:index+1] with difference = diff
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1
        return max(dp.values())
