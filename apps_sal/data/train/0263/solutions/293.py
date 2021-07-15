class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: [],  # 5 has no neighbors
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
        }
        memo = {}
        def dp_memo(S, N):
            if (S, N) in memo:
                return memo[(S, N)]
            elif N == 0:
                return 1
            else:
                moves = 0
                for neigh in neighbors[S]:
                    moves += dp_memo(neigh, N - 1)
                memo[(S, N)] = moves
                return moves
        result = 0
        for i in range(0, 10):
            result += dp_memo(i, n - 1)
        return result % ((10 ** 9) + 7)
            

