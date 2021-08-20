class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max_satisfaction = 0
        for i in range(0, len(satisfaction)):
            curr_satisfaction = 0
            timestamp = 1
            for j in range(i, len(satisfaction)):
                curr_satisfaction += satisfaction[j] * timestamp
                timestamp += 1
            max_satisfaction = max(max_satisfaction, curr_satisfaction)
        return max_satisfaction
