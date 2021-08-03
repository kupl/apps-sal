class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # Brute Force.
        teams = 0
        for i in range(0, len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):

                    if (i < j < k) and (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        teams += 1

        return teams
