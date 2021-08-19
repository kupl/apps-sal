class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def getSum(k):
            res = 0
            for n in nums:
                if n % k == 0:
                    res += n // k
                else:
                    res += n // k + 1
            return res
        (l, r) = (max(sum(nums) // threshold, 1), max(1, sum(nums)))
        while l < r:
            m = (l + r) // 2
            if getSum(m) > threshold:
                l = m + 1
            else:
                r = m
        return l
