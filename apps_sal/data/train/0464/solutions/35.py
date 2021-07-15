import math
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for x in range(0, n+1):
            ans += math.floor(x/2)
        return ans
