from itertools import combinations


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = list(combinations(rating, 3))
        count = 0
        for i in res:
            if i[0] > i[1] > i[2] or i[0] < i[1] < i[2]:
                count += 1
        return count
