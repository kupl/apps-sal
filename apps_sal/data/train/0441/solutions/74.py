class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i, ans = 1, 0
        while N > i * (i - 1) // 2:
            if (N - i * (i - 1) // 2) / i == (N - i * (i - 1) // 2) // i:
                ans += 1
            i += 1
        return ans
