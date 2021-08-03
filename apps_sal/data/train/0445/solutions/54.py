class Solution:
    def _util(self, nums):
        min_heap, max_heap = [], []
        for i, x in enumerate(nums):
            heapq.heappush(min_heap, (x, i))
            if len(min_heap) > 4:
                heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-x, i))
            if len(max_heap) > 4:
                heapq.heappop(max_heap)
        return sorted([x for x, i in set(min_heap + [(-x, i) for x, i in max_heap])])

    def minDifference(self, nums: List[int]) -> int:
        lst = self._util(nums) if len(nums) > 100 else sorted(nums)
        result = lst[-1] - lst[0]
        x = min(4, len(lst))
        for i in range(x):
            curr = lst[-x + i] - lst[i]
            result = min(result, curr)
        return result
