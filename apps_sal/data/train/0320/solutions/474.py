class Solution:
    def minOperations(self, nums: List[int]) -> int:
        memo = {0: (0, 0)}  # (+1,*2)

        def helper(num):
            if num not in memo:
                if num % 2 == 1:
                    a, b = helper(num - 1)
                    memo[num] = (a + 1, b)
                else:
                    a, b = helper(num // 2)
                    memo[num] = (a, b + 1)
            return memo[num]
        a = b = 0
        for num in nums:
            tmpa, tmpb = helper(num)
            a += tmpa
            b = max(b, tmpb)
        return a + b
