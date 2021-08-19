class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        t = 0
        for ele in nums:
            ele = str(bin(ele))[2:]
            res += ele.count('1')
            t = max(t, len(ele) - 1)
        return res + t
