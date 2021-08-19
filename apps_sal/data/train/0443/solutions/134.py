class Solution:

    def numTeams(self, rating: List[int]) -> int:
        result = 0
        n = len(rating)
        for i in range(0, n - 2):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    if rating[k] > rating[i] and rating[k] < rating[j]:
                        result += 1
                    elif rating[k] < rating[i] and rating[k] > rating[j]:
                        result += 1
        return result
