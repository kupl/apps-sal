class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def helper(div):
            output = 0
            for n in nums:
                if n % div == 0:
                    output += n // div
                else:
                    output += n // div + 1
            if output <= threshold:
                return True
            return False
        nums.sort()
        (l, r) = (1, max(nums))
        while l < r:
            mid = l + (r - l) // 2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l
