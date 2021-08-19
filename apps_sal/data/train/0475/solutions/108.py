class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        out = []
        for i in range(n):
            heapq.heappush(out, (nums[i], i))
        ans = 0
        for i in range(1, right + 1):
            x = heapq.heappop(out)
            if i >= left:
                ans += x[0]
            if x[1] + 1 < len(nums):
                heapq.heappush(out, (x[0] + nums[1 + x[1]], 1 + x[1]))
        return ans % (10 ** 9 + 7)
