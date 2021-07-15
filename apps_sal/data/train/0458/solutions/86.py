class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums) % p
        if s == 0:
            return 0
        n = len(nums)
        ans = n
        
        pre = {}
        pre[0] = -1
        cur = 0
        for i, x in enumerate(nums):
            cur += x
            cur %= p
            need = (cur - s + p) % p
            if need in pre:
                ans = min(ans, i - pre[need])
            pre[cur] = i
        
        return ans if ans < n else -1
        

