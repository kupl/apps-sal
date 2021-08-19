class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def bs(mid):
            sum_val = 0
            for i in nums:
                sum_val += math.ceil(i / mid)
                if sum_val > threshold:
                    return False
            return True
        l = 1
        r = 10 ** 6
        while l <= r:
            mid = (l + r) // 2
            if bs(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
