class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        beneficial = [s for s in satisfaction if s >= 0]
        negative = [s for s in satisfaction if s < 0]
        for s in reversed(negative):
            if calc_satisfaction([s] + beneficial) > calc_satisfaction(beneficial):
                beneficial.insert(0, s)
        return calc_satisfaction(beneficial)


def calc_satisfaction(dishes):
    total = 0
    for (i, s) in enumerate(dishes):
        total += (i + 1) * s
    return total
