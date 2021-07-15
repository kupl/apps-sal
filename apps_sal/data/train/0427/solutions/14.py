class Solution:
    def countOrders(self, n: int) -> int:
        l = 2
        num = 1
        for i in range(2, n+1):
            num = sum(num*(l-hole+1) for hole in range(l+1))
            l += 2
        return num % (10**9+7)
