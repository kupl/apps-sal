class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        for i in range(1, len(satisfaction)):
            current = satisfaction[i]
            for j in range(i, 0, -1):
                satisfaction[j] = current * (j + 1) + satisfaction[j - 1]
            satisfaction[0] = max(satisfaction[0], current)
        return max(max(satisfaction), 0)
