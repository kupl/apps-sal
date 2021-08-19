class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        best = 0
        for i in range(len(satisfaction)):
            count = 1
            val = 0
            for j in range(i, len(satisfaction)):
                val += satisfaction[j] * count
                count += 1
            best = max(best, val)
        return best
