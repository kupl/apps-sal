class Solution:
    # https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/801679/Simple-elegant-code-with-explanation-and-example
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 2 or K == 5:
            return -1
        remainder = 0
        for i in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if not remainder:
                return i
        return -1
