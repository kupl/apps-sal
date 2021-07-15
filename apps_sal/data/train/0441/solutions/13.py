class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        n = 1
        ans = 0
        
        def helper(n):
            return n * (n + 1) / 2
        
        while helper(n) <= N:
            ans += int((N - helper(n)) % n == 0)
            n += 1
        
        return ans

