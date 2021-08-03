class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans, constants, div = 0, 0, 0
        for i in range(N):
            div = i + 1
            constants = constants + i
            quotient, remainder = divmod((N - constants), div)
            if quotient <= 0:
                return ans
            if not remainder:
                ans += 1
        return ans
