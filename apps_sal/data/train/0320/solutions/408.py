class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def minSteps(num):
            if num == 0:
                return 0
            if num == 1:
                return 1

            if num in memo:
                return memo[num]

            if num & 1:
                num_ways = 1 + minSteps(num - 1)
            else:
                num_ways = minSteps(num // 2)

            memo[num] = num_ways

            return memo[num]

        def countPowerOfTwo(num):
            if num < 2:
                return 0
            cnt = 1
            cur = 2
            while cur * 2 <= num:
                cnt += 1
                cur <<= 1

            return cnt

        memo = {}
        res = countPowerOfTwo(max(nums))
        for num in nums:
            res += minSteps(num)

        return res
