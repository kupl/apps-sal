from math import comb


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        sum = 0
        for i in range(len(rating) - 2):
            for j in range(i, len(rating) - 1):
                for k in range(j, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        sum += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        sum += 1
        return sum
