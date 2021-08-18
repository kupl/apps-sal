class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = [[nums[0], 0]]
        maxheap = [[-nums[0], 0]]
        left = -1
        res = 1
        for i, val in enumerate(nums[1:]):
            j = i + 1
            while len(maxheap) and len(minheap) and max(val, -maxheap[0][0]) - min(val, minheap[0][0]) > limit:
                if val == max(val, -maxheap[0][0]):
                    v, l = heapq.heappop(minheap)
                elif minheap and val == min(val, minheap[0][0]):
                    v, l = heapq.heappop(maxheap)
                left = max(l, left)
            res = max(j - left, res)
            heapq.heappush(minheap, [val, j])
            heapq.heappush(maxheap, [-val, j])
        return res
