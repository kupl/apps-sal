class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if not nums:
            return 0
        
        r = sum(nums) % p
        if r == 0:
            return 0
        dic = {}
        mod = {0:{-1}}
        dic[-1] = 0
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] % p == r:
                return 1
            dic[i] = dic[i-1]+nums[i]
            
            m = dic[i] % p
            t = (m - r + p) % p
            if t in mod:
                last = max(mod[t])
                res = min(res, i-last)
        
            if m not in mod:
                mod[m] = set()
                
            mod[m].add(i)
        
        print(mod)
        print(r)
        if res == len(nums):
            return -1
        
        return res
        
        # # O(n^2) TLE
        # # removed subarray len
        # for i in range(1, len(nums)):
        #     # subarray start index
        #     for j in range(0, len(nums) - i + 1):
        #         _sum = dic[i+j-1] - dic[j-1]
        #         if _sum % p == r:
        #             return i
                
        
        return -1
