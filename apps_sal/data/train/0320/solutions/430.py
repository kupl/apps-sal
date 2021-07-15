class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        new_nums = sorted(nums, reverse=True)
        while len(new_nums) > 0:
            if new_nums[-1] == 0:
                new_nums.pop(len(new_nums) - 1)
            elif new_nums[-1] == 1:
                new_nums.pop(len(new_nums) - 1)
                result += 1
            else:
                flag = True
                for i in range(len(new_nums)):
                    if new_nums[i] & 0x1 == 1:
                        new_nums[i] -= 1
                        result += 1
                        flag = False
                if flag:
                    for i in range(len(new_nums)):
                        new_nums[i] >>= 1
                    result += 1
        return result
