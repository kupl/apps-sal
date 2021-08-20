class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ret = nums[0]
        for i in range(1, len(nums)):
            remove = i - k - 1
            while remove >= heap[0][1]:
                heapq.heappop(heap)
            cur = max(0, -heap[0][0]) + nums[i]
            ret = max(ret, cur)
            heapq.heappush(heap, (-cur, i))
        return ret
