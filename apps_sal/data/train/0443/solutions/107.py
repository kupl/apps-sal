class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        count += 1
                    elif rating[i] < rating[j] and rating[j] < rating[k]:
                        count += 1
        return count
