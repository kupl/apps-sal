class Solution:

    def numTeams(self, rating: List[int]) -> int:
        combs = combinations(rating, 3)
        return sum((c[0] < c[1] < c[2] or c[0] > c[1] > c[2] for c in combs))
