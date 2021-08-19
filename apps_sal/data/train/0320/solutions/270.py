class Solution:

    def minOperations(self, nums: List[int]) -> int:
        result = 0
        result_num_div = 0
        for i in range(len(nums)):
            num_div = 0
            while nums[i] > 0:
                if nums[i] % 2 == 1:
                    result += 1
                    nums[i] -= 1
                if nums[i] > 1:
                    num_div += 1
                nums[i] /= 2
            result_num_div = max(result_num_div, num_div)
        return result + result_num_div
