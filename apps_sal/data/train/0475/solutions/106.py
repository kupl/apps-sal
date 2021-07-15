class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sz = len(nums)
        temp = []
        for i,val in enumerate(nums):
            heapq.heappush(temp,(val,i))

        ans = 0
        for i in range(1, right + 1):
            cur = heapq.heappop(temp)
            if i >= left:
                ans = ans + cur[0]
            if cur[1] < sz - 1:
                heapq.heappush(temp, (cur[0] + nums[cur[1] + 1], cur[1] + 1))

        return ans % 1_000_000_007
