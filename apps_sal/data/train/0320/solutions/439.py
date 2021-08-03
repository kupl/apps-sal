class Solution:
    def minOperations(self, nums: List[int]) -> int:

        valid = {0: 0}
        for i in range(31):
            valid[2 ** i] = i

        ans = 0
        max_multi_step = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                ans += 1
            else:
                continue
            one_step, multi_step = 0, 0

            while nums[i] not in valid:
                if nums[i] & 1:
                    one_step += 1
                    nums[i] -= 1
                else:
                    multi_step += 1
                    nums[i] //= 2

            ans += one_step
            max_multi_step = max(max_multi_step, multi_step + valid[nums[i]])

        ans += max_multi_step
        return ans
