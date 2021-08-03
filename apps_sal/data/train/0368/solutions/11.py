class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        if satisfaction[0] >= 0:
            return calc_satisfaction(satisfaction)

        min_val = max(s for s in satisfaction if s < 0)
        min_index = satisfaction.index(min_val)
        '''
        for s in satisfaction:
            if s >= 0:
                beneficial.append(s) # [0, 2, 5]
            else:
                negative.append(s)  # [-3, -2]
        '''
        curr_satisfaction = calc_satisfaction(satisfaction[min_index + 1:])
        while True:
            min_index -= 1
            temp_satisfaction = calc_satisfaction(satisfaction[min_index + 1:])
            if temp_satisfaction > curr_satisfaction:
                curr_satisfaction = temp_satisfaction
            else:
                break

        return curr_satisfaction


def calc_satisfaction(dishes):
    total = 0
    for i, s in enumerate(dishes):
        total += (i + 1) * s
    return total
