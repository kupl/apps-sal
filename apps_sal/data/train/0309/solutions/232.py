# class Solution:
#     def longestArithSeqLength(self, arr: List[int]) -> int:
#         if not arr:
#             return 0
        
#         dp = [collections.defaultdict(lambda : 1) for _ in range(len(arr))]
#         ret = 1
#         for i in range(len(arr)):
#             for j in range(i):
#                 dp[i][arr[i] - arr[j]] = 1 + dp[j][arr[i] - arr[j]]
#                 ret = max(ret, dp[i][arr[i] - arr[j]])
        
#         return ret

class Solution:
   def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
