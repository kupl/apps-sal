class Solution:
    def longestArithSeqLength(self, A):
        dp = dict()
        for endi, endv in enumerate(A[1:], start = 1):
            for starti, startv in enumerate(A[:endi]):
                diff = endv - startv
                if (starti, diff) in dp:
                    dp[(endi, diff)] = dp[(starti, diff)] + 1
                else:
                    dp[(endi, diff)] = 2
        return max(dp.values())
    
class Solution:
    def longestArithSeqLength(self, A):
        dp = dict()
        for starti, startv in enumerate(A):
            for endi, endv in enumerate(A[starti+1:], start = starti+1):
                diff = endv - startv
                if (starti, diff) in dp:
                    dp[(endi, diff)] = dp[(starti, diff)] + 1
                else:
                    dp[(endi, diff)] = 2
        return max(dp.values())
    
class Solution:
    def longestArithSeqLength(self, A):
        N = len(A)
        dp = [{0:1} for _ in range(N)]
        for end in range(1, N):
            for start in range(end):
                diff = A[end] - A[start]
                if diff in dp[start]:
                    dp[end][diff] = dp[start][diff] + 1
                else:
                    dp[end][diff] = 2
        return max(max(dp[end].values()) for end in range(1, N))
    
class Solution:
    def longestArithSeqLength(self, A):
        ans = 2
        n = len(A)
        index = {}
        dp = [[2] * n for i in range(n)]
        
        for i in range(n-1):
            for j in range(i+1, n):
                first = A[i] + A[i] - A[j]
                if first in index:
                    dp[i][j] = dp[index[first]][i] + 1
                    #ans = max(ans, dp[i][j])
                    if dp[i][j] > ans: ans = dp[i][j]
            index[A[i]] = i
        return ans

