class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        pq = [(-nums[0], 0)]
        res = nums[0]
        for i in range(1, len(nums)):
            rm = i - k - 1
            while pq[0][1] <= rm:
                heapq.heappop(pq)
            cur = max(-pq[0][0], 0) + nums[i]
            res = max(res, cur)
            heapq.heappush(pq, (-cur, i))
        return res
