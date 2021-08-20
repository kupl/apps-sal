class Solution:

    def minOperations(self, nums: List[int]) -> int:

        @lru_cache(None)
        def helper(num):
            if num < 2:
                return (num, 0)
            (a, b) = helper(num // 2)
            return (a + num % 2, b + 1)
        a = b = 0
        for num in nums:
            (tmpa, tmpb) = helper(num)
            a += tmpa
            b = max(b, tmpb)
        return a + b
