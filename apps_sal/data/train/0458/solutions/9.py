class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        s = sum(nums)
        k = s % p
        if not k:
            return 0
        d = {0: -1}
        sumJ = 0
        res = float('inf')
        for (i, num) in enumerate(nums):
            sumJ += num
            '\n            (sumJ-sumI)%p=k\n            sumJ-sumI=n*p+k\n            sumI=sumJ-np-k\n            sumI%p=(sumJ-np-k)%p=(sumJ%p-np%p-k%p)%p=(sumJ%p-k%p)%p\n            '
            sumI_mod_p = (sumJ % p - k % p) % p
            if sumI_mod_p in d:
                res = min(res, i - d[sumI_mod_p])
            d[sumJ % p] = i
        return res if res < n else -1
