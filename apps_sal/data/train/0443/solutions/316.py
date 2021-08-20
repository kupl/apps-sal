class Solution:

    def numTeams(self, rating: List[int]) -> int:
        teams_all = list(itertools.combinations(rating, 3))
        valid_teams = []
        for team in teams_all:
            if team[0] > team[1] > team[2] or team[0] < team[1] < team[2]:
                valid_teams.append(team)
        return len(valid_teams)
