class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        new = sorted(rating)
        if new == rating:
            return len(rating)
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k] or (rating[i] > rating[j] and rating[j] > rating[k]):
                        count = count + 1
        return count
