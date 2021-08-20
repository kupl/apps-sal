class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        q = []
        worker = []
        for (s, e) in zip(speed, efficiency):
            worker.append([s, e])
        (ans, speeds, minEff) = (0, 0, float('inf'))
        for (s, e) in sorted(worker, key=lambda x: -x[1]):
            if len(q) < k:
                heapq.heappush(q, [s, e])
                speeds += s
                minEff = min(minEff, e)
            elif s > q[0][0]:
                (ts, te) = heapq.heappop(q)
                speeds = speeds - ts + s
                minEff = e
                heapq.heappush(q, [s, e])
            ans = max(ans, speeds * minEff)
        return ans % (10 ** 9 + 7)
