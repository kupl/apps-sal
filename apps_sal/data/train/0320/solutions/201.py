class Solution:

    def minOperations(self, nums: List[int]) -> int:
        actions = 0
        n = len(nums)
        while True:
            odd_flag = False
            for i in range(n):
                if nums[i] % 2 == 1:
                    actions += 1
                    nums[i] -= 1
                    odd_flag = True
            if all((num == 0 for num in nums)):
                break
            if odd_flag:
                continue
            for i in range(n):
                nums[i] //= 2
            actions += 1
            if all((num == 0 for num in nums)):
                break
        return actions
