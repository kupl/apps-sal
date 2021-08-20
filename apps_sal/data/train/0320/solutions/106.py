class Solution:

    def toZero(self, n):
        extra = 0
        pwr2 = 0
        while n > 0:
            if n % 2:
                n -= 1
                extra += 1
            else:
                n = n / 2
                pwr2 += 1
        return [extra, pwr2]

    def minOperations(self, nums: List[int]) -> int:
        maxPwr2 = 0
        extras = 0
        for n in nums:
            a = self.toZero(n)
            maxPwr2 = max(maxPwr2, a[1])
            extras += a[0]
        return extras + maxPwr2
