class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        maxlen = 0
        binlen = 0
        for num in nums:
            binlen = 0
            while num != 0:
                if num % 2 != 0:
                    ones += 1
                    num -= 1

                if num != 0:
                    num //= 2
                    binlen += 1
            maxlen = max(maxlen, binlen)

        return maxlen + ones
