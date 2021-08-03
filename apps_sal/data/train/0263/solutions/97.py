class Solution:
    moveMap = {
        0: [4, 6],
        1: [8, 6],
        2: [7, 9],
        3: [8, 4],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    def nextMoves(self, n: int):
        return self.moveMap[n]

    def knightDialer(self, n: int) -> int:
        modulo = 1000000007
        if n < 0:
            return 0
        counts = [1] * 10
        moves = len(self.moveMap)
        while n > 1:
            newCounts = [0] * 10
            for i in range(moves):
                for m in self.nextMoves(i):
                    newCounts[m] += counts[i]
            counts = newCounts
            n -= 1
        return sum(counts) % modulo
