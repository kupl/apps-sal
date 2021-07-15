import itertools
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        candidates = list(combinations(rating, 3))
        return sum([candidate[0] <= candidate[1] <= candidate[2] or candidate[0] >= candidate[1] >= candidate[2] for candidate in candidates])
