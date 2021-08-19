class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(0, len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        count += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        count += 1
        return count
