from itertools import combinations


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        valid = 0
        for i in combinations(rating, 3):
            if (i[0] < i[1]):
                if (i[1] < i[2]):
                    valid += 1
            elif (i[0] > i[1]):
                if (i[1] > i[2]):
                    valid += 1
        return valid
