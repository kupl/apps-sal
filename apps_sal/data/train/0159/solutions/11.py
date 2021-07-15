class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        _max = collections.deque()
        res = max(nums)
        
        for i in range(n):
            if len(_max) and _max[0][0] > 0:
                val = nums[i] + _max[0][0]
            else:
                val = nums[i]
            while len(_max) and _max[-1][0] < val: _max.pop()
            _max.append((val, i))
            res = max(val, res)
        
            if _max[0][1] <= i-k:
                _max.popleft()
    
        return res

