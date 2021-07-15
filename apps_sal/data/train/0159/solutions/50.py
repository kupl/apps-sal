class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = [(-nums[0], 0)]
        res = nums[0]
        dp = [0] * n
        
        for i in range(1, n):
            while q and i - q[0][1] > k:
                heapq.heappop(q)
                
            t = max(nums[i] - q[0][0], nums[i])
            res = max(res, t)
            heapq.heappush(q, (-t, i))
            
        return res
