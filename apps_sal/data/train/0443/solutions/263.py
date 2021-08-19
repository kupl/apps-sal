class Solution:

    def numTeams(self, rating: List[int]) -> int:
        team = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        team = team + 1
                    elif rating[i] < rating[j] and rating[j] < rating[k]:
                        team = team + 1
        return team
