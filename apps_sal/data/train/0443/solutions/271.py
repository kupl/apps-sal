class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    total += any([rating[i] < rating[j] < rating[k], rating[i] > rating[j] > rating[k]])
        return total
