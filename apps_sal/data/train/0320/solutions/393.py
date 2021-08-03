class Solution:
    def minOperations(self, nums) -> int:
        steps = 0

        while True:
            # make even
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    steps += 1

            # check if done
            remaining = 0
            for i in range(len(nums)):
                if nums[i] > 0:
                    remaining += 1
            if remaining == 0:
                return steps

            # divide
            for i in range(len(nums)):
                nums[i] /= 2
            steps += 1
