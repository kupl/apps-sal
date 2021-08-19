import heapq


class Solution:

    def insert_heap(self, h, n, right):
        if len(h) < right:
            heapq.heappush(h, -n)
        elif -h[0] > n:
            heapq.heappop(h)
            heapq.heappush(h, -n)

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = []
        for i in range(len(nums)):
            s = nums[i]
            self.insert_heap(h, s, right)
            for j in range(i + 1, len(nums)):
                s += nums[j]
                self.insert_heap(h, s, right)
        res = 0
        for i in range(right - left + 1):
            res += -heapq.heappop(h)
        return res % 1000000007
