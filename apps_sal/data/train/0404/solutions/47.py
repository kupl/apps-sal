class Solution:
    def mean(self, l):
        return sum(l)/len(l)
    
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        DP = [self.mean(A[i:n]) for i in range(n)]
        
        for k in range(K-1):
            for i in range(n):
                for j in range(i+1, n):
                    DP[i] = max(DP[i], self.mean(A[i:j]) + DP[j])

        return DP[0]
        
        
        
        
#         n = len(A)
#         if n==1:
#             return A[0]
#         if K==1:
#             return self.mean(A)
#         DP = {}
        
#         for i in range(1, n-K+2):
#             if i>n-1:
#                 break
#             if K==2:
#                 DP[i] = self.mean(A[:i]) + self.mean(A[i:])
#             else:
#                 DP[i] = self.mean(A[:i]) + self.largestSumOfAverages(A[i:], K-1)
#         return max(list(DP.values()))


