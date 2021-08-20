class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        temp = c = 0
        while True:
            for i in range(n):
                if nums[i] == 1:
                    c += 1
                    nums[i] = 0
                elif nums[i] % 2 == 1:
                    nums[i] -= 1
                    c += 1
                if nums[i] == 0:
                    temp += 1
            if temp == n:
                return c
            temp = 0
            for i in range(n):
                nums[i] = int(nums[i] / 2)
            c += 1
