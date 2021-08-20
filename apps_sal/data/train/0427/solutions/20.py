class Solution:

    def countOrders(self, n: int) -> int:

        def solve(remaining, pending):
            if remaining == 0 and pending == 1:
                return 1
            if memo[remaining][pending] != -1:
                return memo[remaining][pending]
            count = 0
            if remaining > 0:
                count += remaining * solve(remaining - 1, pending + 1)
            if pending > 0:
                count += pending * solve(remaining, pending - 1)
            count %= MOD
            memo[remaining][pending] = count
            return count
        MOD = 10 ** 9 + 7
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return solve(n, 0)
