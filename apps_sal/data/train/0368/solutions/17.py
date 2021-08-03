class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sorted_satis = sorted(satisfaction)
        max_satis = sorted_satis[-1]

        if max_satis <= 0:
            return 0

        def calculate_satisfaction(start_index):
            s = 0
            for i in range(len(sorted_satis) - start_index):
                s += (i + 1) * sorted_satis[start_index + i]
            return s

        max_satisfaction = -1

        for i in range(len(sorted_satis)):
            max_satisfaction = max(max_satisfaction, calculate_satisfaction(i))
            if sorted_satis[i] >= 0:
                return max_satisfaction

        return max_satisfaction
