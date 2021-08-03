class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isThres(m):
            tsum = 0
            for n in nums:
                tsum += n // m
                if n % m > 0:
                    tsum += 1
            if tsum <= threshold:
                return True

        l, r = 1, sum(nums)

        while l < r:
            m = l + r >> 1
            if isThres(m):
                r = m
            else:
                l = m + 1

        return l
