class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:

        def gcd(a, b):
            if b > a:
                a, b = b, a
            while (b > 0):
                r = divmod(a, b)[1]
                a = b
                b = r
            return a

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0] == 1

        ans = nums[0]

        for i in range(1, len(nums)):
            ans = gcd(ans, nums[i])
            if ans == 1:
                return True

        return ans == 1
