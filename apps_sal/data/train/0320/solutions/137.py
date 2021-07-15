class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        _max = 0
        for i in nums:
            bit = 0
            while i>0:
                res += i&1
                i >>= 1
                bit += 1
            _max = max(bit,_max)
        return res+_max-1
