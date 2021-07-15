class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        
        maxSoFar = 0
        
        for curr in range(len(A)):
            for prev in range(curr):
                difference = A[curr] - A[prev]
                dp[curr][difference] = max(dp[curr][difference], dp[prev][difference] + 1)
                maxSoFar = max(maxSoFar, dp[curr][difference])
        
        return maxSoFar + 1

