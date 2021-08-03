import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hq = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(hq)
        c = 0
        s = 0
        for i in range(right):
            v, i = heapq.heappop(hq)
            if c >= left - 1:
                s += v
            c += 1
            if i + 1 < len(nums):
                heapq.heappush(hq, (v + nums[i + 1], i + 1))
        return s % (10 ** 9 + 7)
