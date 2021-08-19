class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p
        if mod == 0:
            return 0
        pos = {}
        pos[0] = -1
        s = 0
        ans = len(nums)
        for (i, num) in enumerate(nums):
            s = (s + num) % p
            pmod = (s - mod) % p
            if pmod in pos:
                ans = min(ans, i - pos[pmod])
            pos[s] = i
        return ans if ans < len(nums) else -1
