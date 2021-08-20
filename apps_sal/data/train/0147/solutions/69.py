class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        vals = [(speed[i], efficiency[i]) for i in range(n)]
        vals.sort(reverse=True, key=lambda x: x[1])
        speed = 0
        ans = 0
        pq = []
        for i in range(n):
            heapq.heappush(pq, vals[i][0])
            speed += vals[i][0]
            if len(pq) > k:
                speed -= heapq.heappop(pq)
            ans = max(ans, speed * vals[i][1])
        return ans % (10 ** 9 + 7)
