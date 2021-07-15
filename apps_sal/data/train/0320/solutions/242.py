class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def minSteps(num):
            if num == 1:
                return 1            
            if num in memo:
                return memo[num]
            # count only odd numbers
            memo[num] = minSteps(num // 2) if num % 2 == 0 else 1 + minSteps(num - 1)
            
            return memo[num]
        
        def countPowerOfTwo(num):
            if num < 2: 
                return 0
            cnt, cur = 1, 2
            while cur * 2 <= num:
                cnt += 1
                cur <<= 1
            
            return cnt
        
        memo = {}
        # count the power of two for once and only once
        # because it these number can be used by the \"multiply by 2\" operation to all elements
        res = countPowerOfTwo(max(nums))
        for num in nums:
            if num == 0:
                continue
            res += minSteps(num)
        
        return res
