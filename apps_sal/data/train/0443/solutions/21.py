class Solution:
    def numTeams(self, rating: List[int]) -> int:
        team = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                if rating[j] > rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            team = team + 1
                elif rating[j] < rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] < rating[j]:
                            team = team + 1
        return team
