class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7

        if n == 1:
            return 10
        curr_total = []
        last_step_totals = [1 for _ in range(10)]

        for i in range(n - 1):
            curr_total = [0 for _ in range(10)]

            for i in range(10):
                for jump_location in jumps[i]:
                    curr_total[i] += last_step_totals[jump_location]
            last_step_totals = curr_total
        return sum(curr_total) % mod
