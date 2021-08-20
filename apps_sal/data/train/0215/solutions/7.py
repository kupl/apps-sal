class Solution:

    def gcd(self, a: int, b: int) -> int:
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def isGoodArray(self, nums: List[int]) -> bool:
        lowest = nums[0]
        for i in nums[1:]:
            lowest = self.gcd(lowest, i)
        return lowest == 1
