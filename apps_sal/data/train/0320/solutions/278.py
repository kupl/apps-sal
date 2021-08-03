from copy import deepcopy


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def modify(arr, op, idx):
            if op == 0:
                arr[idx] = arr[idx] - 1
            elif op == 1:
                for i, num in enumerate(arr):
                    arr[i] = num // 2

        zeros = [0] * len(nums)
        ans = 0
        while True:
            for i, num in enumerate(nums):
                if num % 2 == 1:
                    nums[i] = num - 1
                    ans += 1

            if nums == zeros:
                return ans
            else:
                modify(nums, 1, 0)
                ans += 1

        return ans
