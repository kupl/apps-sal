class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums, len(nums))
        count = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            while (nums[i] + nums[j] > target) & (i < j):
                j -= 1
            if (i > j) | (nums[i] * 2 > target):
                break
            print(j - i, end=' & ')
            count += 2 ** (j - i)
        print(i, j)
        return count % (10 ** 9 + 7)
