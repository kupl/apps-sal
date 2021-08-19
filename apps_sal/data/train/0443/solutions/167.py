class Solution:

    def numTeams(self, rating: List[int]) -> int:
        from itertools import combinations
        com = list(combinations(rating, 3))
        cnt = 0
        if len(rating) < 2:
            return 0
        for t in com:
            if t[0] > t[1] > t[2] or t[0] < t[1] < t[2]:
                cnt += 1
        return cnt
