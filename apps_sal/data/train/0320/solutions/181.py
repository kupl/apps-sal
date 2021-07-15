class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while not all(n == 0 for n in nums):
            div = 0
            for i, n in enumerate(nums):
                if n & 1:
                    ans += 1
                    n -= 1
                if n > 0:
                    div = 1
                    n //= 2
                nums[i] = n
            ans += div
        return ans
