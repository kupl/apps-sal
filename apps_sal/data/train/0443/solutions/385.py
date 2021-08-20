class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        for i in range(n):
            for k in range(i + 2, n):
                if rating[i] < rating[k]:
                    teams += len([r for r in rating[i + 1:k] if rating[i] < r < rating[k]])
                else:
                    teams += len([r for r in rating[i + 1:k] if rating[i] > r > rating[k]])
        return teams
