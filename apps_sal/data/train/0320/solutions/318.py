class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        mul = [0] * n
        for i in range(n):
            while nums[i] != 0:
                if nums[i] % 2:
                    res += 1
                    nums[i] -= 1
                else:
                    mul[i] += 1
                    nums[i] //= 2

        return res + max(mul)
