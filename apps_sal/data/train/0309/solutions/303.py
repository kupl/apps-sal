from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(dict) # { index: {difference: steps} }
        max_cnt = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                difference = A[i] - A[j]
                length = dp[j].get(difference, 1) + 1
                dp[i][difference] = dp[j].get(difference, 1) + 1
                max_cnt = max(max_cnt, length)
        
        return max_cnt
                

