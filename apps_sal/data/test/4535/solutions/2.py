class Solution:
    def hammingWeight(self, n: int) -> int:
        strn = str(bin(n))
        # print(strn)
        return strn.count('1')
