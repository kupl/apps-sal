class Solution:
    def minOperations(self, nums: List[int]) -> int:
        valid = {0: 0}
        for i in range(31):
            valid[2 ** i] = i

        ans = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                ans += 1

        max_val = float('-inf')
        need_step = [0] * len(nums)
        max_multiply_step = 0
        for i in range(len(nums)):
            one_step, multiply_step = 0, 0
            while nums[i] not in valid:
                if nums[i] & 1:
                    one_step += 1
                    nums[i] -= 1
                else:
                    multiply_step += 1
                    nums[i] //= 2

            max_multiply_step = max(max_multiply_step, multiply_step + valid[nums[i]])
            ans += one_step

        ans += max_multiply_step

        return ans
