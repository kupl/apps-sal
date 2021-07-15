class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        combo = []
        for i in range(n):
            heapq.heappush(combo, (-efficiency[i], -speed[i]))
        tmp = []
        ans, currsum = 0, 0
        
        while combo:
            curre, currs = heapq.heappop(combo)
            heapq.heappush(tmp, -currs)
            currsum -= currs
            if len(tmp) > k:
                currsum -= heapq.heappop(tmp)
            ans = max(ans, -currsum * curre)
        return ans % MOD
