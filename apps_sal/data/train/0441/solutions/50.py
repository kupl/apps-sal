class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        ans = 0
        k = 1
        while True:
            a, b = divmod(N, 2 * k)
            if a >= k and b == k:
                ans += 1
            elif a < k:
                break
            a, b = divmod(N, 2 * k + 1)
            if a >= k + 1 and b == 0:
                ans += 1
            elif a < k + 1:
                break
            k += 1
        return ans + 1
