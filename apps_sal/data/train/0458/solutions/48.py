class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        if not nums:
            return 0
        r = sum(nums) % p
        if r == 0:
            return 0
        dic = {}
        mod = {0: {-1}}
        dic[-1] = 0
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] % p == r:
                return 1
            dic[i] = dic[i - 1] + nums[i]
            m = dic[i] % p
            t = (m - r + p) % p
            if t in mod:
                last = max(mod[t])
                res = min(res, i - last)
            if m not in mod:
                mod[m] = set()
            mod[m].add(i)
        print(mod)
        print(r)
        if res == len(nums):
            return -1
        return res
        return -1
