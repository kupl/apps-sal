class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:

        def euclid(a, b):
            (q, r) = (max(a, b), min(a, b))
            while r > 1 and q > 0:
                (r, q) = (q % r, r)
            return r if r > 0 else q
        if len(nums) == 1:
            return True if nums[0] == 1 else False
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = euclid(nums[i], nums[i - 1])
            if nums[i] == 1:
                return True
        return False
