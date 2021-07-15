class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tar = sum(nums) % p
        if tar == 0:
            return 0
        rec = {0: -1}
        cur = 0
        res = len(nums)
        for i, v in enumerate(nums):
            cur = (cur + v) % p
            t = (cur - tar + p) % p
            if t in rec:
                res = min(res, i - rec[t])
            rec[cur] = i
        return -1 if res == len(nums) else res

