from itertools import combinations


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for tupl in combinations(rating, 3):
            if tupl[0] < tupl[1] < tupl[2] or tupl[0] > tupl[1] > tupl[2]:
                result += 1
        return result
