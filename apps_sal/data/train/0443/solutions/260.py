class Solution:
    def numTeams(self, rating: List[int]) -> int:

        teams = []

        for i in range(0, len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    curr = (rating[i], rating[j], rating[k])
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        teams.append(curr)
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        teams.append(curr)

        return len(teams)
