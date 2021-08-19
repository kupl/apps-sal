class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def minSteps(num):
            if num == 1:
                return 1
            if num in memo:
                return memo[num]
            memo[num] = minSteps(num // 2) if num % 2 == 0 else 1 + minSteps(num - 1)
            return memo[num]

        def countPowerOfTwo(num):
            if num < 2:
                return 0
            (cnt, cur) = (1, 2)
            while cur * 2 <= num:
                cnt += 1
                cur <<= 1
            return cnt
        memo = {}
        res = countPowerOfTwo(max(nums))
        for num in nums:
            if num == 0:
                continue
            res += minSteps(num)
        return res
