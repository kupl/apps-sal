class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7
        memo = {}

        def helper(n, starting, memo):
            if (n, starting) in memo:
                return memo[(n, starting)]
            if n == 1:
                return 1
            if n == 2:
                return len(jumps[starting])
            sum = 0
            for jump_location in jumps[starting]:
                sum += helper(n - 1, jump_location, memo)
            memo[(n, starting)] = sum
            return sum

        total_jumps = 0
        for i in range(10):
            if i == 5 and n != 1:
                continue
            total_jumps += helper(n, i, memo)
        return total_jumps % mod
