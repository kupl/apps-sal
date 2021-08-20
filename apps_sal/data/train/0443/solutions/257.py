from itertools import combinations
import numpy as np


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        rating = np.array(rating)
        for i in range(len(rating)):
            if sum(rating[i] < rating[i + 1:]) >= 2:
                soldiers = [x for x in rating[i + 1:] if x > rating[i]]
                comb_soldiers = combinations(soldiers, 2)
                count = count + len([comb for comb in comb_soldiers if list(comb) == sorted(comb)])
            if sum(rating[i] > rating[i + 1:]) >= 2:
                soldiers = [x for x in rating[i + 1:] if x < rating[i]]
                comb_soldiers = combinations(soldiers, 2)
                count = count + len([comb for comb in comb_soldiers if list(comb) == sorted(comb, reverse=True)])
        return count
