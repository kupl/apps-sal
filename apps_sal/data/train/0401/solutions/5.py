class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        zero, one, two = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        one[0] = two[0] = float('-inf')
        for i in range(1, n + 1):
            if nums[i - 1] % 3 == 0:
                zero[i] = zero[i - 1] + nums[i - 1]
                one[i] = one[i - 1] + nums[i - 1] if one[i - 1] > 0 else 0
                two[i] = two[i - 1] + nums[i - 1] if two[i - 1] > 0 else 0
            elif nums[i - 1] % 3 == 1:
                zero[i] = max(two[i - 1] + nums[i - 1], zero[i - 1])
                two[i] = max(two[i - 1], one[i - 1] + nums[i - 1])
                one[i] = max(one[i - 1], zero[i - 1] + nums[i - 1])
            else:
                zero[i] = max(one[i - 1] + nums[i - 1], zero[i - 1])
                two[i] = max(zero[i - 1] + nums[i - 1], two[i - 1])
                one[i] = max(two[i - 1] + nums[i - 1], one[i - 1])
        return zero[-1]
