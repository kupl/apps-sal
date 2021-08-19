class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        (n, result, p1, p2, m) = (len(nums), 0, 0, len(nums) - 1, 1000000007)
        nums.sort()
        while p1 <= p2:
            if nums[p1] + nums[p2] <= target:
                result = (result + pow(2, p2 - p1, m)) % m
                p1 += 1
            else:
                p2 -= 1
        return result
