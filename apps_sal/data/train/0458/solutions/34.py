class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tar = sum(nums) % p
        if tar == 0:
            return 0
        n = len(nums)
        pos = collections.defaultdict(lambda: -n)
        pos[0] = -1
        cur, res = 0, n
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            res = min(res, i - pos[(cur - tar) % p])
            pos[cur] = i
        return res if res < n else -1
