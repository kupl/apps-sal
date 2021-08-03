import heapq
import math


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        h = []
        ans = -math.inf

        for i, a in enumerate(A):
            if h:
                ans = max(ans, a - i - h[0])
            heapq.heappush(h, -i - a)
        return ans
