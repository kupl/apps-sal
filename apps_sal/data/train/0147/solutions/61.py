import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        arr = zip(efficiency, speed)
        arr = sorted(arr, key=lambda x: (-x[0], -x[1]))
        pq = []
        maxSoFar, currSum = 0, 0

        for eff, sp in arr:

            currSum += sp
            heapq.heappush(pq, sp)
            if len(pq) == k + 1:
                currSum -= heapq.heappop(pq)

            maxSoFar = max(maxSoFar, currSum * eff)

        return maxSoFar % ((10**9) + 7)
