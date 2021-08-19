class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        m = 0
        while len(satisfaction) > 0:
            s = sum((satisfaction[i] * (i + 1) for i in range(len(satisfaction))))
            m = max(s, m)
            satisfaction = satisfaction[1:]
        return m
