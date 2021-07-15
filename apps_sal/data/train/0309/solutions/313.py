from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[i][A[i]-A[j]]=max(dp[j][A[i]-A[j]]+1,2)
        return max([val for _ in dp for __,val in _.items()])
