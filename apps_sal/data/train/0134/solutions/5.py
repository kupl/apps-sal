class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        digits = []
        M = N + 1
        while M > 0:
            digits.append(M % 10)
            M //= 10

        part_1 = 0
        prod = 9
        i_1 = 9

        n = len(digits)

        for i in range(n - 1):
            part_1 += prod
            if i_1 > 1:
                if i > 0:
                    i_1 -= 1
                prod *= i_1
        i_1 = 9
        seen = set([])
        cols = [0 for i in range(10)]
        while len(digits) > 0:
            digit = digits.pop()
            if len(digits) == n - 1:
                prod = digit - 1
            else:
                prod = digit - cols[digit]
            j_1 = i_1
            for i in range(len(digits)):
                prod *= j_1
                j_1 -= 1
            i_1 -= 1
            part_1 += prod

            if digit in seen:
                break
            else:
                seen.add(digit)
            for i in range(digit + 1, 10):
                cols[i] += 1
        return N - part_1
