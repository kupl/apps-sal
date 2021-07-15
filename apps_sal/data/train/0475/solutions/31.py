from queue import PriorityQueue

class Solution:
    def rangeSum(self, nums: List[int], total: int, left: int, right: int) -> int:
        pq = PriorityQueue()
        for i, n in enumerate(nums):
            pq.put((n, i))
        j, ans = 0, 0
        while not pq.empty():
            n, i = pq.get()
            j += 1
            if j >= left and j <= right:
                ans = (ans + n) % 1000000007
            elif j > right:
                return ans
            if i<total-1:
                pq.put((n+nums[i+1], i+1))
        return ans

