class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        n = 2
        while((2 * N + n - n * n) > 0):
            start = (2 * N + n - n**2) / (2 * n)
            if(start - int(start) == 0):
                count += 1
            n += 1
        return count
