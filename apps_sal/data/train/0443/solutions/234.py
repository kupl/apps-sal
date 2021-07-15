class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        teams = set()
        for i in range(0, len(rating) - 2):
            for j in range(i + 1, len(rating) -1):
                for k in range(j + 1, len(rating)):
                    if (rating[i] < rating[j] < rating[k]):
                        teams.add((i, j, k))
                    if (rating[i] > rating[j] > rating[k]):
                        teams.add((i, j, k))
                        
        return len(teams)
