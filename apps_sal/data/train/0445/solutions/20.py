class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        maxHeap, minHeap = [], []
        import heapq
        for e in nums:
            heappush(maxHeap, e)
            heappush(minHeap, e * -1)
            if len(maxHeap) > 4:
                heappop(maxHeap)
                heappop(minHeap)
        minHeap = sorted([-1 * e for e in minHeap])
        res = float('inf')
        for i in range(4):

            res = min(res, heappop(maxHeap) - minHeap[i])

        return res
