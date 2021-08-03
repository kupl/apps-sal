class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        while True:
            for idx in range(0, len(nums)):
                if nums[idx] % 2 == 1:
                    nums[idx] -= 1
                    steps += 1
            if sum(nums) == 0:
                break
            nums = [int(x / 2) for x in nums]
            steps += 1

        return steps
