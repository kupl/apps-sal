class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] << 1
        nums.sort()
        res = 0
        j = n - 1
        for i in range(j + 1):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i > j:
                continue
            '\n            In subarray nums[i~j]:\n            min = nums[i], max = nums[j]\n            nums[i] + nums[j] <= target\n            {nums[i], (j - i - 1 + 1 values)}\n            Any subset of the right part gives a valid subsequence \n            in the original array. And There are 2^(j - i) ones.\n            '
            res += 2 ** (j - i)
        return res % (10 ** 9 + 7)
