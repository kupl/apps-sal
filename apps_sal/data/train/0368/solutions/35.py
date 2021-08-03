class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        if (max(sat) < 0):
            return 0
        arr = []
        sat.sort(reverse=True)
        for i in range(len(sat)):
            sun = 0
            for j in range(len(sat) - i):
                sun += sat[j] * (len(sat) - i - j)
            arr.append(sun)
        print(arr)
        return max(arr)
