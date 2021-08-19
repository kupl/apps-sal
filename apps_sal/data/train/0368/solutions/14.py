class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[0] >= 0:
            return calc_satisfaction(satisfaction)
        min_val = -sys.maxsize
        min_index = None
        print(satisfaction)
        for (i, v) in enumerate(satisfaction):
            if 0 > v > min_val:
                min_index = i
                min_val = v
        print((min_val, min_index))
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
    for (i, s) in enumerate(dishes):
        total += (i + 1) * s
    return total
