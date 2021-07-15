class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        queue = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(queue)
        
        ans = 0
        for i in range(1, right + 1):
            val, ind = heapq.heappop(queue)
            
            if i >= left: ans += val
            if ind + 1 < len(nums):
                heapq.heappush(queue, (val + nums[ind + 1], ind + 1))
        
        return ans % (10 ** 9 + 7)
