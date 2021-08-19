import itertools


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        return sum((1 for (ri, rj, rk) in itertools.combinations(rating, 3) if ri < rj < rk or ri > rj > rk))
