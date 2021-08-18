class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0

        nums.sort()
        a1, a2, a3, a4 = nums[:4]
        print(a1, a2, a3, a4)
        b4, b3, b2, b1 = nums[-4:]

        return min(b4 - a1, b3 - a2, b2 - a3, b1 - a4)
