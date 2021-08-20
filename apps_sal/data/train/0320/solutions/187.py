class Solution:

    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            for i in range(len(nums)):
                if nums[i] != 0:
                    if nums[i] & 1 != 0:
                        nums[i] -= 1
                        cnt += 1
                    nums[i] = nums[i] >> 1
            if sum(nums) == 0:
                return cnt
            cnt += 1
        return cnt
        '\n        # Backwards!!!!\n        # Some problems is hard to solve forward, but can be easy if solved backwards!!!!\n        # Change nums to arr\n        \n        step = 0\n        \n        while True:\n            for i in range(len(nums)):\n                if nums[i]%2 != 0:\n                    nums[i] = nums[i] - 1\n                    step += 1\n                nums[i] = nums[i]//2\n            if sum(nums) == 0:\n                return step\n            step += 1\n        '
