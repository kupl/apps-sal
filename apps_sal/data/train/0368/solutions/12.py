class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = 0
        beneficial = deque()
        negative = []

        if satisfaction[0] > 0:
            return calc_satisfaction(satisfaction)

        for s in satisfaction:
            if s >= 0:
                beneficial.append(s)  # [0, 2, 5]
            else:
                negative.append(s)  # [-3, -2]

        curr_satisfaction = calc_satisfaction(beneficial)
        for s in reversed(negative):
            beneficial.appendleft(s)
            temp_satisfaction = calc_satisfaction(beneficial)
            if temp_satisfaction > curr_satisfaction:
                curr_satisfaction = temp_satisfaction
            else:
                beneficial.popleft()
                break

        return curr_satisfaction


def calc_satisfaction(dishes):
    total = 0
    for i, s in enumerate(dishes):
        total += (i + 1) * s
    return total
