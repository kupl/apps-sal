class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for p in range(len(position)):
            times.append([(target - position[p]) / speed[p], position[p]])

        times.sort()

        maxTime = 0
        res = 0
        # print(times)
        for t in range(len(times) - 1, -1, -1):
            if times[t][1] >= maxTime:
                res += 1
            maxTime = max(times[t][1], maxTime)

        return res
