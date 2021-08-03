class Solution:
    def countOrders(self, n: int) -> int:
        F = [0, 1]

        for i in range(2, n + 1):
            one_way = i * 2 - 1
            F.append(one_way * F[i - 1] * i)

        return F[n] % (pow(10, 9) + 7)
