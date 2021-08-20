class Solution:

    def modify(self, arr, op, idx):
        if op == 0:
            arr[idx] = arr[idx] - 1
        if op == 1:
            for i in range(len(arr)):
                arr[i] = arr[i] / 2

    def minOperations(self, nums: List[int]) -> int:
        result = [0 for _ in range(len(nums))]
        operations = 0
        while nums != result:
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    self.modify(nums, 0, i)
                    operations += 1
            if nums == result:
                return operations
            self.modify(nums, 1, i)
            operations += 1
        return operations
