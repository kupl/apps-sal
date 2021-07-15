class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         maxScore = 0 

#         for i in range(0,len(A)):
#             for j in range(i+1,len(A)):
#                 val = A[i] + A[j] + i - j 
#                 if val > maxScore:
#                     maxScore = val 
#         return maxScore

        K    = A[0]
        best = float('-inf')
        for j in range(1,len(A)):
            x    = A[j]
            best = max(best, K + x - j )
            K    = max(K   , x + j     )
        return best
