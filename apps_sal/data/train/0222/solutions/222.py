class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
#         d = set()
#         n = len(A)
#         for c in A:
#             d.add(c)
            
#         max_l = 0
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 a = A[i]
#                 b = A[j]
#                 count = 0
#                 while (a+b) in d:
#                     count += 1
#                     a,b = b,a+b
#                 max_l = max(max_l, count+2)
                
#         if max_l >= 3:
#             return max_l
#         return 0
    
        dp = collections.defaultdict(int)
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])
