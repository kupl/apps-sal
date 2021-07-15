class Solution:
    def consecutiveNumbersSum(self, x: int) -> int:
        ans = 1
        for n in range(2, 100000):
            a = 2 * x - n * (n - 1)
            b = 2 * n
            if a < b:
                break
            if a % b == 0:
                ans += 1
        return ans
