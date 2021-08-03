class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        n = nums[0]

        for i in nums:
            n = gcd(i, n)

            if n == 1:
                return True
        return False
