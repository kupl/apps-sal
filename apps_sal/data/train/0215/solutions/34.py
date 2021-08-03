class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]

        for i in range(1, len(nums)):
            res = math.gcd(res, nums[i])
            if res == 1:
                return True

        return res == 1
