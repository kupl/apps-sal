# 尝试策略: 将数组内所有数字变成偶数然后处理/2，重复此过程直到有结果
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tot_step = 0
        while True:
            not_zero = False
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                not_zero = True
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    tot_step += 1
            # Already reach the result, stop now.
            not_zero = False
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                not_zero = True
                nums[i] = nums[i] / 2
            if not_zero == False:
                break
            tot_step += 1
        return tot_step
