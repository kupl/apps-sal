class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        l = 1
        out = 0
        while (1 + l) * l / 2 <= N:
            b = (2 * N + l ** 2 - l) / (2 * l)
            a = b + 1 - l
            if a == int(a) and b == int(b):
                out += 1
            l += 1
        return out
