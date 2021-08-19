from math import gcd
from functools import reduce


class Solution:

    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(lambda x, y: gcd(x, y), nums) == 1
