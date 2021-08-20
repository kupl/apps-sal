class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(0, len(rating) - 2):
            for j in range(i, len(rating) - 1):
                for k in range(j, len(rating)):
                    if rating[i] < rating[j] < rating[k]:
                        count += 1
                    elif rating[i] > rating[j] > rating[k]:
                        count += 1
        return count
