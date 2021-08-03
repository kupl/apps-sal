class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        teams = []
        for i1, r1 in enumerate(ratings):
            for si2, r2 in enumerate(ratings[i1 + 1:]):
                i2 = i1 + 1 + si2
                for r3 in ratings[i2 + 1:]:
                    teams.append((r1, r2, r3))
        n = 0
        for i, j, k in teams:
            if i < j < k or i > j > k:
                n += 1

        return n
