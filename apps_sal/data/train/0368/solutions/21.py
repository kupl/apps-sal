class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        output = 0
        result = 0
        for i in range(len(satisfaction)):
            output += satisfaction[i] * i
        for i in range(0, len(satisfaction)):
            for j in range(i, len(satisfaction)):
                result += satisfaction[j] * (j - i + 1)
            if output < result:
                output = result
            result = 0
        if output < 0:
            output = 0
        return output
