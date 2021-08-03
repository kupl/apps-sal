class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                if ((num >> i) & 1):
                    count += 1
            ans |= ((count % 3) << i)
        if ans >= 2**31:
            ans -= 2**32
        return ans
