def oneMore(length: int) -> int:
    if length < 2:
        return 1
    return int(length * (length + 1) / 2 + length + 1)


class Solution:

    def countOrders(self, n: int) -> int:
        acc = 1
        for i in range(0, n * 2, 2):
            acc *= oneMore(i)
            acc %= int(1000000000.0 + 7)
        return acc
