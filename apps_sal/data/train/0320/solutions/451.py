class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cou = [0] * len(nums)
        count = 0
        for i in range(len(nums)):
            while(nums[i] > 0):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    count += 1
                else:
                    nums[i] = nums[i] // 2
                    cou[i] += 1
        res = max(cou) + count

        return res
