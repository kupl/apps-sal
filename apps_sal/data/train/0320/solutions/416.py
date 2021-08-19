class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while sum(nums) != 0:
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            if sum(nums) == 0:
                return count
            flag = False
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    nums[i] //= 2
                    flag = True
            if flag:
                count += 1
        return count
