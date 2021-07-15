class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        
        for i, x in enumerate(A):
            nd = collections.defaultdict(int)
            dp.append(nd)
            for j in range(i):
                curr_diff = x - A[j]
                dp[i][curr_diff] = dp[j][curr_diff] + 1
          
        return max(max(y.values()) for y in dp) + 1
