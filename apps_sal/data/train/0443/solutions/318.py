class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count_teams = 0
        temp_team = []
        all_possible_teams = []
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if i != j and j != k:
                        all_possible_teams.append((rating[i], rating[j], rating[k]))
        for i in all_possible_teams:
            if i[0] < i[1] and i[1] < i[2]:
                count_teams = count_teams + 1
            if i[0] > i[1] and i[1] > i[2]:
                count_teams = count_teams + 1
        return count_teams
