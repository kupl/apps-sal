class Solution:
    def rangeSum1(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            prefix = 0
            for j in range(i, len(nums)):
                prefix += nums[j]
                res.append(prefix)

        res.sort()
        return sum(res[left-1:right]) % 1_000_000_007
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        import heapq
        h = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(h)
        
        ans = 0
        for k in range(1, right + 1):
            val, idx = heapq.heappop(h)
            if k >= left: ans += val
            ## right is 1 more than actual length
            if idx + 1 < len(nums):
                heapq.heappush(h, (val + nums[idx+1], idx+1))
        
        return ans % 1_000_000_007

