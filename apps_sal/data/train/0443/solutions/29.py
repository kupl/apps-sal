class Solution:
    def numTeams(self, rating):
        return sum(x < y < z or x > y > z for x, y, z in combinations(rating, 3))
