class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        count = 0
        while nums != arr:
            check = True
            for x in nums:
                if x % 2 != 0:
                    check = False
            if check == True:
                count += 1
                for x in range(len(nums)):
                    nums[x] = nums[x] // 2
            for x in range(len(nums)):
                if nums[x] % 2 != 0:
                    nums[x] = nums[x] - 1
                    count += 1
        return count
