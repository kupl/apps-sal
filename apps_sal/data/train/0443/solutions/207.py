class Solution:
    def canFormATeam(self, r1: int, r2: int, r3: int) -> bool:
        return (r1 < r2 < r3) or (r1 > r2 > r3)

    def numTeams(self, rating: List[int]) -> int:
        n_teams: int = 0

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if self.canFormATeam(rating[i], rating[j], rating[k]):
                        n_teams += 1

        return n_teams
