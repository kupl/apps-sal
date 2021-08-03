class Solution:
    def minOperations(self, nums: List[int]) -> int:
        o = 0
        m = 0
        a = 0
        for i in nums:
            m = 0
            while(i):
                if(i % 2 == 0):
                    m += 1
                    i //= 2
                else:
                    o += 1
                    i -= 1
            a = max(m, a)
        return o + a
