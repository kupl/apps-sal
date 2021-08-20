class Solution:

    def calc(self, num):
        m = 0
        a = 0
        while num > 0:
            if num & 1:
                a += 1
                num -= 1
            else:
                num = num >> 1
                m += 1
        return (a, m)

    def minOperations(self, nums: List[int]) -> int:
        adds = 0
        mults = 0
        for i in range(len(nums)):
            (a, m) = self.calc(nums[i])
            if mults < m:
                mults = m
            adds += a
        return mults + adds
