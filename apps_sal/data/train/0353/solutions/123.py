class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        j = len(nums) - 1

        for i in range(len(nums)):
            while (nums[i] + nums[j] > target) & (i < j):
                j -= 1

            if (i > j) | (nums[i] * 2 > target):
                break
            count += pow(2, j - i)

        return count % (10**9 + 7)
