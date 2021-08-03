class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            if nums[0] == 1:
                return True
            else:
                return False

        ans = self.gcd(nums[0], nums[1])
        for num in nums[2:]:
            ans = self.gcd(ans, num)
            if ans == 1:
                return True
        return ans == 1

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
