class Solution:

    def knightDialer(self, n: int) -> int:

        MOD = 10**9 + 7

        M = [[0 for i in range(10)] for j in range(n + 1)]

        next_move = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [],
                     6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        def paths(pos, nhop):
            if nhop == 1:
                return 1

            if M[nhop][pos] > 0:
                return M[nhop][pos]

            for j in range(len(next_move[pos])):
                M[nhop][pos] += paths(next_move[pos][j], nhop - 1) % MOD
            return M[nhop][pos]

        ans = 0
        for start in range(10):
            ans = (ans + paths(start, n)) % MOD

        return int(ans)
