class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = range(1, len(rating) + 1)
        teams = list(zip(teams, rating))
        teams_inc = sorted(teams, key=lambda x: x[1])
        teams_dec = sorted(teams, key=lambda x: -x[1])
        ans = 0
        for i in range(0, len(teams) - 2):
            for j in range(i + 1, len(teams) - 1):
                for k in range(j + 1, len(teams)):
                    if teams_inc[i][0] < teams_inc[j][0] < teams_inc[k][0]:
                        ans += 1
        for i in range(0, len(teams) - 2):
            for j in range(i + 1, len(teams) - 1):
                for k in range(j + 1, len(teams)):
                    if teams_dec[i][0] < teams_dec[j][0] < teams_dec[k][0]:
                        ans += 1
        return ans
