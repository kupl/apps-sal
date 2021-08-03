from collections import defaultdict


class Solution:
    def knightDialer(self, n: int) -> int:
        _nextMove = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [],
                     6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        moves = {i: 1 for i in range(10)}

        while n > 1:
            newmoves = defaultdict(int)
            for k, v in moves.items():
                for _next in _nextMove[k]:
                    newmoves[_next] += v
            moves = newmoves
            n -= 1

        return sum(moves.values()) % (10 ** 9 + 7)
