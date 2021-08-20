class Solution:

    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        n = len(rating)
        for i in range(n - 2):
            for j in range(i, n - 1):
                if rating[i] < rating[j] or rating[i] > rating[j]:
                    for k in range(j, n):
                        if rating[i] < rating[j] < rating[k]:
                            teams += 1
                        if rating[i] > rating[j] > rating[k]:
                            teams += 1
        return teams
