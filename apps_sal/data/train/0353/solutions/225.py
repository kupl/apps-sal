class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        pre = [0] * n
        pre[0] = 1
        res = 0
        for i in range(1, n):
            pre[i] = (pre[i - 1] * 2) % mod
                
        start, end = 0, n - 1
        while start <= end:
            if (nums[start] + nums[end] > target):
                end -= 1
            else:
                res = (res + pre[end - start]) % mod
                start += 1
               
            
            
            
        
        return res % mod

