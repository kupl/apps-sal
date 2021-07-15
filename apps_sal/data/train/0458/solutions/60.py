class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        mods = collections.defaultdict(int)
        mods[0] = -1
        cur = 0
        res = float('inf')
        for i, v in enumerate(nums):
            cur = (cur + v) % p
            mods[cur] = i
            want = (cur - need) % p
            if want in mods:
                res = min(res, i - mods[want])
        return res if res != len(nums) else -1
