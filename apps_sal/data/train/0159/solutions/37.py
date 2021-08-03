class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        rec = -nums[0]
        heap = [(-nums[0], 0)]
        for j, n in enumerate(nums[1:]):
            while j + 1 - heap[0][1] > k:
                heapq.heappop(heap)
            cand = -n + heap[0][0] if heap[0][0] <= 0 else -n
            rec = min(rec, cand)
            heapq.heappush(heap, (cand, j + 1))
        return -rec
