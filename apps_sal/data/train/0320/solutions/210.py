class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        while True:
            sol = True
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    c += 1
                if nums[i] != 0:
                    sol = False
            if sol:
                break

            c += 1
            nums = [x // 2 for x in nums]
        return c
