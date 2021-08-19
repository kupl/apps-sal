class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        count = 0
        while start <= end:
            if nums[start] + nums[end] <= target:
                count += 2 ** (end - start) % 1000000007
                start += 1
            else:
                end -= 1
        for i in range(end + 1, len(nums)):
            if nums[i] * 2 <= target:
                count += 1
            else:
                break
        return count % 1000000007
