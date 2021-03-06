class Solution:

    def knightDialer(self, n: int) -> int:
        kd_key = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        memo = dict()
        out = 0
        for i in range(10):
            out += self.dial(i, n, kd_key, memo)
        return out % int(1000000000.0 + 7)

    def dial(self, pos, n, kd_key, memo):
        if n == 1:
            return 1
        out = 0
        for next_pos in kd_key[pos]:
            if (next_pos, n - 1) in memo:
                out += memo[next_pos, n - 1]
            else:
                out += self.dial(next_pos, n - 1, kd_key, memo)
        memo[pos, n] = out
        return out
