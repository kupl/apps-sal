class Solution:
    def minOperations(self, n: int) -> int:

        ops = 0
        for i in range(n):
            ops += abs((2 * i + 1) - n)

        return ops // 2
#         (1 + n) / 2 * n * 2 + n

#         n2 + n + 1

#         (n - 1)


#         1 + 2n - 2 + 1 / 2 * n


#         n^2 / n
