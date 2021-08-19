import itertools


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for item in itertools.combinations(rating, 3):
            if item[0] < item[1] and item[1] < item[2]:
                ans += 1
            if item[0] > item[1] and item[1] > item[2]:
                ans += 1
        return ans
