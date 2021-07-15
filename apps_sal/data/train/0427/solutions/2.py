class Solution:
    def countOrders(self, n: int) -> int:
        if n <= 1:
            return n
        num_spots = (n*2) - 1
        return (((num_spots*(num_spots+1))//2) * self.countOrders(n-1)) % ((10**9)+7)

