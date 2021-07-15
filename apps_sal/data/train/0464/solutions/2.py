class Solution:
    def minOperations(self, n: int) -> int:
        out = 0
        diff = (n - 1)
        while diff > 0:
            out += diff
            diff -= 2
        
        return out

