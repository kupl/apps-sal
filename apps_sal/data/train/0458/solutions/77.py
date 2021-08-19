class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        a = [0]
        for x in nums:
            a.append((a[-1] + x) % p)
        f = {0: 0}
        k = a[-1]
        if k == 0:
            return 0
        ret = 1000000000
        for i in range(1, len(a)):
            k2 = a[i]
            k1 = (k2 - k + p) % p
            if k1 in f and i - f[k1] < ret:
                ret = i - f[k1]
            f[k2] = i
        if ret >= len(nums):
            return -1
        return ret
