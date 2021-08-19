class Solution:

    def maxPerformance(self, n, speed, efficiency, k):
        ls = list(zip(speed, efficiency))
        ls.sort(key=lambda x: -x[1])
        HEAP = []
        tsum = 0
        ans = 0
        for i in range(n):
            if i >= k:
                (speed, efficiency) = heapq.heappop(HEAP)
                tsum -= speed
            heapq.heappush(HEAP, ls[i])
            tsum += ls[i][0]
            ans = max(ans, tsum * ls[i][1])
        return ans % 1000000007
