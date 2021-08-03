class Solution:
    def countOrders(self, n: int) -> int:
        def solve(remaining, pending):
            # Base case: no remaining orders and one pending order
            if remaining == 0 and pending == 1:
                return 1

            # Memoization case
            if memo[remaining][pending] != -1:
                return memo[remaining][pending]

            count = 0

            # Recursive case 1: start a new order, there are remaining ways to do so
            if remaining > 0:
                count += remaining * solve(remaining - 1, pending + 1)

            # Recursive case 2: end an order; there are pending ways to do so
            if pending > 0:
                count += pending * solve(remaining, pending - 1)

            count %= MOD
            memo[remaining][pending] = count
            return count

        MOD = 10**9 + 7
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return solve(n, 0)
