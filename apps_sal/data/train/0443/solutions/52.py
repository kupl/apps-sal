class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        while len(rating) > 0:
            r = rating.pop(0)
            counter += countDown(rating, r, 1)
            counter += countUp(rating, r, 1)
        return counter


def countUp(rating, value, num_in_team):
    if len(rating) == 0:
        return 0
    counter = 0
    for i, num in enumerate(rating):
        if num > value and num_in_team == 2:
            counter += 1
        elif num > value:
            counter += countUp(rating[i:], num, 2)
    return counter


def countDown(rating, value, num_in_team):
    if len(rating) == 0:
        return 0
    counter = 0
    for i, num in enumerate(rating):
        if num < value and num_in_team == 2:
            counter += 1
        elif num < value:
            counter += countDown(rating[i:], num, 2)
    return counter
