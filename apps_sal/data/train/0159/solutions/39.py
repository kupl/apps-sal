import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        dp = [None] * n
        for i in range(n):
            best = None
            while len(heap) > 0:
                val, idx = heap[0]
                val *= (-1)

                if i - idx <= k:
                    best = val
                    break

                heapq.heappop(heap)

            dp[i] = nums[i]
            if best is not None and dp[i] < best + nums[i]:
                dp[i] = best + nums[i]

            heapq.heappush(heap, (-dp[i], i))
        return max(dp)
