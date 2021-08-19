class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for (a, soldier_1) in enumerate(rating):
            for (b, soldier_2) in enumerate(rating[a + 1:]):
                for (c, soldier_3) in enumerate(rating[a + b + 1:]):
                    if soldier_1 < soldier_2 < soldier_3:
                        count += 1
                    if soldier_1 > soldier_2 > soldier_3:
                        count += 1
        return count
