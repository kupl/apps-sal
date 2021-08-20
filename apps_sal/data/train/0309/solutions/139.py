class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        Maintain a dictionary of differences at each position.
        The keys are going to be (position, diff)

        Compare each value with all the values after it
        calculate the diff and store in the dictionary using the equation in the solution.
        This equation is the crux of the solution.

        Do d dry run with example for better understanding
        https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274611/JavaC%2B%2BPython-DP
        """
        if not A:
            return 0
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())
