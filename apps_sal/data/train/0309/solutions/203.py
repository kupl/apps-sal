class Solution:
    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
#     def longestArithSeqLength(self, A: List[int]) -> int:
#         m = {}
        
#         m[A[1] + A[1]-A[0]] = (2,A[1]-A[0])
#         for i in range(2, len(A)):
#             if A[i] in m:
#                 counter, d = m[A[i]]
#                 del m[A[i]]
#                 m[A[i]+d] = (counter+1, d)
#             else:
#                 for j in range(0, i):
#                     d = A[i]-A[j]
#                     m[A[i]+d] = (2,d)
#         # print(m)
#         return max([counter for counter,_ in list(m.values())])

