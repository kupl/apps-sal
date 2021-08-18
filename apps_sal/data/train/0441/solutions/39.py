class Solution:
    def consecutiveNumbersSum(self, x: int) -> int:
        ans = 1
        for n in range(2, 100000):

            a = x - n * (n - 1) // 2
            b = n
            if a < b:
                break
            if a % b == 0:
                ans += 1
        return ans
