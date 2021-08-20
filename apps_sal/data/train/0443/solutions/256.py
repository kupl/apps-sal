class Solution:

    def numTeams(self, rating: List[int]) -> int:
        total = 0
        n = len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        total = total + 1
        return total
