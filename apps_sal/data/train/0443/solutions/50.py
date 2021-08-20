class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        num_valid_teams = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        num_valid_teams += 1
        return num_valid_teams
