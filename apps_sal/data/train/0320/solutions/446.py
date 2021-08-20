class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        while True:
            zero_count = 0
            i = 0
            while i < n:
                if nums[i] & 1 > 0:
                    break
                elif nums[i] == 0:
                    zero_count += 1
                i += 1
            if zero_count == n:
                return result
            if i == n:
                for j in range(n):
                    nums[j] = nums[j] // 2
                result += 1
            for j in range(i, n):
                if nums[j] & 1:
                    nums[j] -= 1
                    result += 1
        return result
