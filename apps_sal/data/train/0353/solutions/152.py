class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i, j, count = 0, n - 1, 0
        while i <= j:
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j:
                count += 1 << (j - i)
            i += 1
        return count % (10 ** 9 + 7)
