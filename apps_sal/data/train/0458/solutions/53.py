class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        t = sum(nums) % p
        if not t:
            return 0
        (d, s, a) = ({0: -1}, 0, len(nums))
        for (i, x) in enumerate(nums):
            s = (s + x) % p
            tt = (s - t) % p
            if tt in d:
                a = min(a, i - d[tt])
            d[s] = i
        return -1 if a == len(nums) else a
