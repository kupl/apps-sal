class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if max(satisfaction) <= 0:
            return 0
        satisfaction.sort()
        if satisfaction[0] > 0:
            output = 0
            for (i, v) in enumerate(satisfaction):
                output += (i + 1) * v
            return output
        min_val = min((i for i in satisfaction if i >= 0))
        min_index = satisfaction.index(min_val)
        temp_satisfaction = satisfaction[min_index:]
        prev = -1
        current_sum = 0
        while current_sum > prev and len(temp_satisfaction) <= len(satisfaction):
            prev = current_sum
            current_sum = 0
            for (i, v) in enumerate(temp_satisfaction):
                current_sum += (i + 1) * v
            min_index -= 1
            temp_satisfaction.insert(0, satisfaction[min_index])
        return prev if prev > current_sum else current_sum
