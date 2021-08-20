class Solution:

    def minOperations(self, nums: List[int]) -> int:
        divied2 = 0
        res = 0
        for i in nums:
            temp = 0
            while i > 0:
                if i % 2 == 0:
                    i //= 2
                    temp += 1
                else:
                    i -= 1
                    res += 1
                divied2 = max(divied2, temp)
        return res + divied2
