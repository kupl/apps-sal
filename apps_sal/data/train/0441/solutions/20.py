class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for k in range (1, int(sqrt(2 * N)) + 1):
            if 2 * N % k == 0:
                x = 2 *N // k - k - 1
                if x % 2 == 0 and x >= 0:
                    ans += 1
        return ans 
