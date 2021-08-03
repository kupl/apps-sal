class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def proc(nums):
            cnt = 0
            for i in range(len(nums)):
                if nums[i] % 2 > 0:
                    nums[i] -= 1
                    cnt += 1
            if cnt == 0:
                for i in range(len(nums)):
                    nums[i] //= 2
            return max(cnt, 1)

        ops = 0
        while sum(nums) > 0:
            ops += proc(nums)
        return ops
