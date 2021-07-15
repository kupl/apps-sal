import bisect as bi
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if p == 1:
            return 0
        total_mod = 0
        seen_mods = {}
        for i in range(len(nums)):
            total_mod += nums[i] % p
            total_mod = total_mod % p
            if total_mod not in seen_mods:
                seen_mods[total_mod] = []
            seen_mods[total_mod].append(i)
        if total_mod == 0:
            return 0
        
        l = len(nums)
        sum = 0
        for i in range(-1, len(nums) - 1):
            if i >= 0:
                sum = (sum + nums[i]) % p
            compl = (sum + total_mod) % p
            if compl not in seen_mods:
                continue
            comp_arr = seen_mods[compl]
            next = bi.bisect(comp_arr, i)
            if next < len(comp_arr) and comp_arr[next] - i < l:
                l = comp_arr[next] - i
        if l == len(nums):
            return -1
        else:
            return l
