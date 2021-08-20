class Solution:

    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            positions = 2 * (n - 1) + 1
            all_possib = 0
            for i in range(positions + 1):
                possibilities = positions - i
                all_possib += possibilities
            return all_possib * self.countOrders(n - 1) % 1000000007
