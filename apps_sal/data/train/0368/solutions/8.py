from numpy import dot


def coefficient(arr):
    if len(arr) <= 0:
        return 0
    return dot(arr, list(range(1, len(arr) + 1)))


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        runningSum = 0
        for i in reversed(list(range(len(satisfaction)))):
            runningSum += satisfaction[i]
            if runningSum <= 0:
                return coefficient(satisfaction[i + 1:])
        return coefficient(satisfaction)
