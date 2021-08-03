class Solution:
    def numTeams(self, rating: List[int]) -> int:

        n = len(rating)
        team_sum = 0
        teams = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k]:
                        team_sum += 1
                    if rating[i] > rating[j] > rating[k]:
                        team_sum += 1

        return team_sum
