class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        m = 0
        def bitcount(a):
            cnt = 0
            while a:
                cnt += 1
                a &= a - 1
            return cnt
        
        for num in nums:
            result += bitcount(num)
            m = max(m, num)
        for i in range(32):
            if m > 1:
                result += 1
            else:
                break
            m >>= 1
        return result
        

