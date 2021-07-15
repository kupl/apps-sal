from fractions import gcd
from functools import reduce
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def find_gcd(list):
            x = reduce(gcd, list)
            return x
        if find_gcd(nums)==1:
            return True
        return False


