import heapq


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = [(-nums[0], 0)]
        res = nums[0]
        for i in range(1, len(nums)):
            while i - k - 1 >= queue[0][1]:
                heapq.heappop(queue)
            curr = max(-queue[0][0], 0) + nums[i]
            res = max(res, curr)
            heapq.heappush(queue, (-curr, i))
        return res
