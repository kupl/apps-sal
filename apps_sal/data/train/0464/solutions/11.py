class Solution:
    def minOperations(self, n: int) -> int:
        l, r = 1, 2*(n-1) + 1
        total = 0
        
        while l < r:
            total += (r-l) // 2
            l += 2
            r -= 2
        
        return total
