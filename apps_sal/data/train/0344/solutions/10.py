class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ## https://leetcode.com/problems/delete-columns-to-make-sorted-iii/discuss/205679/C%2B%2BJavaPython-Maximum-Increasing-Subsequence
        
        m = len(A)
        n = len(A[0])
        dp = [1] * n
        res = n-1
        for j in range(1, n):
            for i in range(j):
                k = 0
                while k<m and A[k][i] <= A[k][j]:
                    k += 1
                if k == m and (1+dp[i])>dp[j]:
                    dp[j] = 1+dp[i]
                
                # if all(a[i] <= a[j] for a in A):
                #     dp[j] = max(dp[j], dp[i] + 1)
                
            res = min(res, n-dp[j])
        return res
                    

