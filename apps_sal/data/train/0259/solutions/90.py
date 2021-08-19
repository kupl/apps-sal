class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def ok(mid):
            ans = 0
            for num in nums:
                ans += math.ceil(num / mid)
                if ans > threshold:
                    return False
            return True
        (l, r) = (1, int(1000000.0))
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
