class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        return sum(rating[i] < rating[j] < rating[k]
                   or rating[i] > rating[j] > rating[k]
                   for i in range(n-2)
                   for j in range(i+1, n-1)
                   for k in range(j+1, n))
