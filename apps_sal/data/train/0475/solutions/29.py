from queue import PriorityQueue
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = PriorityQueue()
        sz = len(nums)

        for i, val in enumerate(nums):
            pq.put((val, i))

        ans = 0
        mod = 10 ** 9 + 7
        for i in range(1, right + 1):
            cur = pq.get()
            if i >= left:
                ans = (ans + cur[0]) % mod
            if cur[1] < sz - 1:
                pq.put((cur[0] + nums[cur[1]+1], cur[1] + 1))

        return ans
