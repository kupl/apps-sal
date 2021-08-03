class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        l = 0

        ans = 0

        while l * (l + 1) / 2 < N:
            a = (N - l * (l + 1) / 2) / (l + 1)
            if int(a) - a == 0:
                ans += 1
            l += 1

        return ans
