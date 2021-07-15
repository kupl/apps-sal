class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_score = 0
        scores = [0] *len(A)
        for i in range (1,len(A)):
            if i == 1:
                scores[i] = A[0] - (len(A) - (i - 1))
            else:
                scores[i] = max(A[i - 1] - (len(A) - (i - 1)),scores[i-1])
        
        for j in range (1,len(A)):
            adj_score = (len(A) - j) + scores[j] + A[j]
            if adj_score > max_score:
                max_score = adj_score
        return max_score
            

