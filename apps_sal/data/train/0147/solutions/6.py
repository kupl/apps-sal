class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ls = list(zip(speed, efficiency))
        ls.sort(key=lambda x: -x[1])
        (hq, ssum) = ([], 0)
        ans = 0
        for (i, (s, e)) in enumerate(ls):
            if i >= k:
                (s0, e0) = heapq.heappop(hq)
                ssum -= s0
            heapq.heappush(hq, (s, e))
            ssum += s
            ans = max(ans, ssum * e)
        return ans % 1000000007
