class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm = sum(nums)
        if sm % p == 0:
            return 0
        re = sm % p
        pre = 0
        reMap = {0:-1}
        ret = len(nums)
        for i, n in enumerate(nums):
            pre += n
            now = pre % p
            key = now - re if now - re >= 0 else now - re + p
            if key in reMap:
                ret = min(ret, i - reMap[key])
            reMap[now] = i
        
        return ret if ret != len(nums) else -1
