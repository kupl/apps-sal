class Solution:

    def numTeams(self, rating: List[int]) -> int:
        return sum((1 for k in range(len(rating)) for j in range(k) for i in range(j) if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]))
