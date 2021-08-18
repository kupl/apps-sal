class Solution:
    def hammingWeight(self, n: int) -> int:
        strn = str(bin(n))
        return strn.count('1')
