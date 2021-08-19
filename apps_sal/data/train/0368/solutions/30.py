class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        highScore = 0
        satisfaction.sort(reverse=True)
        for n in range(len(satisfaction)):
            sortedSatisfaction = satisfaction[:len(satisfaction) - n]
            sumSatisfaction = 0
            for i in range(len(sortedSatisfaction)):
                multiplier = len(sortedSatisfaction) - i
                sumSatisfaction += sortedSatisfaction[i] * multiplier
            if sumSatisfaction > highScore:
                highScore = sumSatisfaction
        return highScore
