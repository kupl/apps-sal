class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
#         Explanation
#         dp[index][diff] equals to the length of arithmetic sequence at index with difference diff.

#         Complexity
#         Time O(N^2)
#         Space O(N^2)
        
        n = len(A)
        if n< 2:
            return n
        dp = {}
        for i in range(n):
            for j in range(i+1, n):
                dp[(j, A[j]-A[i])] = dp.get((i, A[j]-A[i]), 1) + 1 # if there is no such key, len is 1 ==> A[i]
        return max(dp.values())
                    

