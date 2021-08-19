class Solution:

    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        for i1 in range(len(rating) - 2):
            for i2 in range(i1 + 1, len(rating) - 1):
                if rating[i1] < rating[i2]:
                    for i3 in range(i2 + 1, len(rating)):
                        teams += rating[i2] < rating[i3]
                elif rating[i1] > rating[i2]:
                    for i3 in range(i2 + 1, len(rating)):
                        teams += rating[i2] > rating[i3]
        return teams
