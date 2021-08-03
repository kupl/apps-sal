from itertools import combinations


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return len([comb for comb in list(combinations(rating, 3)) if (comb[0] < comb[1] and comb[1] < comb[2]) or (comb[0] > comb[1] and comb[1] > comb[2])])
