class Solution:

    def numTeams(self, rating: List[int]) -> int:
        number_of_teams = 0
        if len(rating) < 3:
            return 0
        else:
            for i in range(0, len(rating)):
                for j in range(i + 1, len(rating)):
                    for k in range(j + 1, len(rating)):
                        if rating[i] < rating[j] and rating[j] < rating[k] or (rating[i] > rating[j] and rating[j] > rating[k]):
                            number_of_teams += 1
        return number_of_teams
