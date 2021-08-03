from heapq import heappush, heappop


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = -float('inf')
        queue = list()
        for i, x in enumerate(nums):
            while queue and queue[0][1] < i - k:
                heappop(queue)
            if queue:
                val, idx = queue[0]
                if val < 0:
                    x -= val
            heappush(queue, [-x, i])
            res = max(res, x)
        return res
