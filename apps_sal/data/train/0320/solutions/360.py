class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            s = 0
            for i in range(len(nums)):
                num = nums[i]
                if num & 1:
                    count += 1
                    nums[i] = num - 1
                    s += num - 1
                else:
                    s += num
            if s == 0:
                return count
            nums = [num // 2 for num in nums]
            count += 1
