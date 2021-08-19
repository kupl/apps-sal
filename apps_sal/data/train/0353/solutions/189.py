class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        count = 0
        while start <= end:
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                num_in_between = end - start
                count += 2 ** num_in_between
                count %= 10 ** 9 + 7
                start += 1
        return count
