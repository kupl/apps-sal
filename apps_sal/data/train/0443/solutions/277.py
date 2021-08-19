class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        total += 1
                    elif rating[i] < rating[j] and rating[j] < rating[k]:
                        total += 1
        return total
