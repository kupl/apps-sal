class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        B = (2 * N + 0.25) ** 0.5 + 0.5
        B = ceil(B)
        ans = 0
        for k in range(1, B + 1):
            a = 2 * N - k ** 2
            b = (2 * N - k ** 2) // k
            c = b + 1
            if a % k == 0 and c % 2 == 0:
                m = c // 2
                if m > 0:
                    ans += 1
                    #print(m, k)
        return ans
