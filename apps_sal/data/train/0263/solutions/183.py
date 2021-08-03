class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        LARGEINT = 10**9 + 7
        moves = {1: 2, 2: 1, 4: 2, 7: 2, 8: 1, 0: 1}
        while n > 1:
            new_moves = {
                1: (moves[4] + (2 * moves[8])) % LARGEINT,
                2: moves[7],
                4: (moves[1] + moves[7] + (2 * moves[0])) % LARGEINT,
                7: (moves[4] + (2 * moves[2])) % LARGEINT,
                8: moves[1],
                0: moves[4]
            }
            moves = new_moves
            n -= 1
        return sum(moves.values()) % LARGEINT
