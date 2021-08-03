class Solution:
    def __init__(self):
        self.num_teams = 0

    def numTeams(self, rating: List[int]) -> int:
        for i in range(len(rating)):
            first_soldier = rating[i]
            self.compareFirstSoldier(first_soldier, rating[i:])

        reversed_rating = rating
        reversed_rating.reverse()
        for i in range(len(reversed_rating)):
            first_soldier = reversed_rating[i]
            self.compareFirstSoldier(first_soldier, reversed_rating[i:])

        return self.num_teams

    def compareFirstSoldier(self, soldier_val: int, rating: List[int]) -> None:
        for j in range(len(rating)):
            if soldier_val < rating[j]:
                second_soldier = rating[j]
                self.compareSecondSoldier(second_soldier, rating[j:])

    def compareSecondSoldier(self, soldier_val: int, rating: List[int]) -> None:
        for k in range(len(rating)):
            if soldier_val < rating[k]:
                self.num_teams += 1
