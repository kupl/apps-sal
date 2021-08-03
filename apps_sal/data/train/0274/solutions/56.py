'''
1. example: [8,2,4,7]

- Subarrays can be created by taking one element at a time and moving forward
- difference can be found by finding the difference between two elements in the array. 



'''


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(nums):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
