class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        calls = 0
        while True:
            num_zeros = 0
            odd_index = 0
            for i in range(n):
                if nums[i] % 2 != 0:
                    break
                elif nums[i] == 0:
                    num_zeros += 1
                odd_index += 1
            if num_zeros == n:
                return calls
            if odd_index == n:
                for j in range(n):
                    nums[j] /= 2
                calls += 1
            for j in range(i, n):
                if nums[j] % 2 != 0:
                    nums[j] -= 1
                    calls += 1
