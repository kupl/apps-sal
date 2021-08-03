class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[index][diff]  equals to the length of arithmetic sequence at index with difference diff.
        # O(n^2)
        # A is unsorted

        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1  # A is unsorted, so it is dp.get((i, A[j]-A[i])) not dp.get(j-1, diff)

        return max(dp.values())
