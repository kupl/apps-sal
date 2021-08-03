class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        best = 0
        total = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            for j in range(len(satisfaction) - 1, i - 1, -1):
                total += satisfaction[j]
            best = max(best, total)
        return best
