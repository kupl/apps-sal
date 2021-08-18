class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        minlen = n = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0

        cursum = 0
        dct = {0: -1}

        for i, num in enumerate(nums):
            cursum = (cursum + num) % p
            dct[cursum] = i
            if (cursum - target) % p in dct:
                minlen = min(minlen, i - dct[(cursum - target) % p])

        return -1 if minlen >= n else minlen
