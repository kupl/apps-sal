class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        s = sum(nums)
        res = 0
        while s:
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    res += 1
            s = 0
            nums = list([x for x in nums if x > 0])
            if not nums:
                break
            for i in range(len(nums)):
                nums[i] //= 2
                s += nums[i]
            res += 1
        return res
