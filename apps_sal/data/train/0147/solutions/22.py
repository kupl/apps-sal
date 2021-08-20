import heapq


class Solution:

    def maxPerformance(self, n, speed, efficiency, k):
        engs = []
        heapq.heapify(engs)
        for i in range(n):
            heapq.heappush(engs, (-efficiency[i], speed[i]))
        speedtotal = 0
        totalperf = 0
        current_team = []
        heapq.heapify(current_team)
        for i in range(k):
            temp = heapq.heappop(engs)
            speedtotal += temp[1]
            totalperf = max(totalperf, speedtotal * -temp[0])
            heapq.heappush(current_team, temp[1])
        for j in range(k, n):
            temp = heapq.heappop(engs)
            if temp[1] > current_team[0]:
                speedtotal -= current_team[0]
                speedtotal += temp[1]
                totalperf = max(totalperf, -temp[0] * speedtotal)
                heapq.heappop(current_team)
                heapq.heappush(current_team, temp[1])
        return totalperf % (10 ** 9 + 7)
