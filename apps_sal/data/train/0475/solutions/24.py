class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        from heapq import heapify, heappop, heappush

        heap = [(number, index) for index, number in enumerate(nums)]
        heapify(heap)

        sum_ = 0

        for index in range(1, right + 1, 1):
            number, heap_index = heappop(heap)
            if index >= left:
                sum_ += number
            if heap_index + 1 < len(nums):
                heappush(heap, (number + nums[heap_index + 1], heap_index + 1))

        return sum_ % (10**9 + 7)
