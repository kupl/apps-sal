class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [[num, idx] for (idx, num) in enumerate(nums)]
        heapq.heapify(heap)
        ret_num = 0
        for i in range(1, right + 1):
            (cur, idx) = heapq.heappop(heap)
            if idx < len(nums) - 1:
                heapq.heappush(heap, [nums[idx + 1] + cur, idx + 1])
            if i >= left:
                ret_num += cur
        return ret_num % (10 ** 9 + 7)
