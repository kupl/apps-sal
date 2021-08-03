class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        x = y = z = sys.maxsize
        if n <= 1:
            return n
        if(n % 2 == 0):
            x = 1 + self.minDays(n // 2)
        if(n % 3 == 0):
            y = 1 + self.minDays(n // 3)
        if(n % 3 != 0 or n % 2 != 0):
            z = 1 + self.minDays(n - 1)

        return min(x, y, z)
