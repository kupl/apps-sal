from collections import deque


class Solution:

    def knightDialer(self, n: int) -> int:
        neighborMap = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: (), 6: (1, 7, 0), 7: (2, 6), 8: (3, 1), 9: (2, 4), 0: (4, 6)}

        def neighbors(pos):
            return neighborMap[pos]

        def countSeq():
            prevMoves = [1] * 10
            curMoves = [0] * 10
            curN = 1
            while curN < n:
                curMoves = [0] * 10
                curN += 1
                for pos in range(10):
                    for neighbor in neighbors(pos):
                        curMoves[pos] += prevMoves[neighbor]
                prevMoves = curMoves
            curMoves = prevMoves
            return sum(curMoves)
        return countSeq() % (10 ** 9 + 7)
