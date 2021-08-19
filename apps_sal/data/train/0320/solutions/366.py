class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = 0
        while True:
            zero_count = 0
            i = 0
            while i < n:
                if nums[i] % 2 == 1:
                    break
                elif nums[i] == 0:
                    zero_count += 1
                i += 1
            if zero_count == n:
                return ans
            if i == n:
                for j in range(n):
                    nums[j] //= 2
                ans += 1
            for j in range(i, n):
                if nums[j] % 2 == 1:
                    nums[j] -= 1
                    ans += 1
        return ans
