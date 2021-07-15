# class Solution:
#     def countTriplets(self, A: List[int]) -> int:
#         N, M = 1<<16, 3
#         dp = [[0]*N for _ in range(M+1)]
#         dp[0][-1] = 1
#         for m in range(M):
#             for n in range(N):
#                 for a in A:
#                     dp[m+1][a&n] += dp[m][n]
#         return dp[-1][0]


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        N = len(A)
        ans = 0
        count = collections.Counter()

        for i in range(N):
            for j in range(N):
                count[A[i]&A[j]] += 1
                
        for k in range(N):
            for v in count:
                if A[k] & v == 0:
                    ans += count[v]
        return ans
