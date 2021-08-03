class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x: int, y: int) -> int:
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        result = nums[0]
        for num in nums:
            result = gcd(result, num)

        return result == 1
