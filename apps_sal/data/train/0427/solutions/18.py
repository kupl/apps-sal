class Solution:
    def countOrders(self, n: int) -> int:
        num = 1
        for i in range(2, n + 1):
            num = sum(num * ((i - 1) * 2 - hole + 1) for hole in range((i - 1) * 2 + 1))
        return num % (10**9 + 7)
