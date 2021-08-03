class Solution:
    def numTeams(self, rating: List[int]) -> int:
        comb = list(itertools.combinations(rating, r=3))

        ans = 0
        for tup in comb:
            if tup[0] < tup[1] < tup[2] or tup[0] > tup[1] > tup[2]:
                ans += 1

        return ans
