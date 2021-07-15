class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i = 0
        max_degree = A[i] + i
        max_score = -float('inf')
        
        for j in range(1, len(A)):
            curr_max_score = A[j] - j + max_degree
            max_score = max(max_score, curr_max_score)
            max_degree = max(max_degree, A[j]+j)
            
        return max_score
