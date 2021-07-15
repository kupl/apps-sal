class Solution:
    def numTeams(self, rating: List[int]) -> int:
        num_teams = 0
        for i,r1 in enumerate(rating):
            for j,r2 in enumerate(rating[(i+1):]):
                for k,r3 in enumerate(rating[(i+j+1):]):
                    num_teams += ((r1 < r2 < r3) or (r1 > r2 > r3))
        return num_teams
