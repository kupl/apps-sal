from heapq import heappush, heappop


class Engineer:

    def __init__(self, speed, efficiency):
        self.speed = speed
        self.efficiency = efficiency

    def __str__(self):
        return str(self.speed) + ',' + str(self.efficiency)


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [Engineer(speed[i], efficiency[i]) for i in range(n)]
        engineers.sort(key=lambda x: x.efficiency, reverse=True)
        performance = 0
        maxSpeeds = []
        sumOfSpeeds = 0
        for (index, engineer) in enumerate(engineers):
            heappush(maxSpeeds, [engineer.speed, index, engineer])
            sumOfSpeeds += engineer.speed
            if len(maxSpeeds) > k:
                sumOfSpeeds -= heappop(maxSpeeds)[2].speed
            performance = max(performance, engineer.efficiency * sumOfSpeeds)
        return performance % (10 ** 9 + 7)
