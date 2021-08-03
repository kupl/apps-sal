class Solution:
    def minOperations(self, arr: List[int]) -> int:
        ret, maxx = 0, 0
        import math
        for i in arr:
            maxx = max(maxx, len(bin(i)) - 3)
            ret += bin(i).count('1')
        return ret + maxx
