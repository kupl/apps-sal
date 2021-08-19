class Solution:

    def getGCD(self, x: int, y: int) -> int:
        while y:
            (x, y) = (y, x % y)
        return x

    def getLCM(self, x: int, y: int) -> int:
        return x * y // self.getGCD(x, y)

    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)
        (x, i) = (nums[0], 1)
        while i < n:
            x = self.getGCD(x, nums[i])
            if x == 1:
                return True
            i += 1
        return x == 1
