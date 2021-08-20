class Solution:

    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        if len(rating) < 3:
            return teams
        for i in range(len(rating)):
            first = rating[i]
            for j in range(i + 1, len(rating)):
                second = rating[j]
                for k in range(j + 1, len(rating)):
                    third = rating[k]
                    if first > second and second > third:
                        teams += 1
                    if first < second and second < third:
                        teams += 1
        return teams
