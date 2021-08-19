class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        (i, j) = (0, n - 1)
        while i <= j:
            tot = nums[i] + nums[j]
            if tot <= target:
                count += 2 ** (j - i) % int(1000000000.0 + 7)
                i += 1
            else:
                j -= 1
        return int(count % (1000000000.0 + 7))
