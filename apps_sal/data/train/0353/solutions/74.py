class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        (i, j) = (0, n - 1)
        while i <= j:
            tot = nums[i] + nums[j]
            if tot <= target:
                count += int(2 ** (j - i))
                i += 1
            else:
                j -= 1
        return count % int(1000000000.0 + 7)
