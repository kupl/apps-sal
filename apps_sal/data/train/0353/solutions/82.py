class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] <= target:
                res += pow(2, end - start)
                start += 1
            else:
                end -= 1

        if nums[start] * 2 <= target:
            res += 1

        _, res = divmod(res, pow(10, 9) + 7)
        return res
