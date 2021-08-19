from itertools import combinations


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        c = 0
        k = list(combinations(rating, 3))
        for i in k:
            if i[0] < i[1] and i[1] < i[2] or (i[0] > i[1] and i[1] > i[2]):
                c += 1
        return c
