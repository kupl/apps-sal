class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         maxScore = 0 

#         for i in range(0,len(A)):
#             for j in range(i+1,len(A)):
#                 val = A[i] + A[j] + i - j 
#                 if val > maxScore:
#                     maxScore = val 
#         return maxScore
        best = 0
        i = 0
        for j in range(1, len(A)):
            s1 = A[i] + A[j] + i - j
            s2 = A[j] + A[j-1] - 1 
            if s2 > s1:
                i = j - 1
            best = max(best, s1, s2) 
        return best
