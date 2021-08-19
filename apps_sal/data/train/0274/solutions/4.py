from heapq import *


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minH = []
        maxH = []
        l = 0
        ans = 0
        for r, n in enumerate(nums):
            heappush(minH, (n, r))
            heappush(maxH, (-n, r))
            while -maxH[0][0] - minH[0][0] > limit:
                l = min(maxH[0][1], minH[0][1]) + 1
                while maxH[0][1] < l:
                    heappop(maxH)
                while minH[0][1] < l:
                    heappop(minH)
            # print(l, r, maxH, minH)
            ans = max(ans, r - l + 1)
        return ans
