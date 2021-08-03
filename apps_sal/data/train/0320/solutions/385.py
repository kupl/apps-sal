class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        while True:
            zero_c = 0
            i = 0
            while i < n:
                if nums[i] % 2 == 1:
                    break
                elif nums[i] == 0:
                    zero_c += 1
                i += 1

            if zero_c == n:
                return res

            if i == n:
                for j in range(n):
                    nums[j] = nums[j] // 2
                res += 1

            for j in range(i, n):
                if nums[j] % 2 == 1:
                    nums[j] -= 1
                    res += 1

        return res
