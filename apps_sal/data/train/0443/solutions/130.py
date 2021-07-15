from itertools import combinations

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return len([(x, y, z) for x, y, z in list(combinations(rating, 3)) if (x < y and y < z) or (x > y and y > z)])
