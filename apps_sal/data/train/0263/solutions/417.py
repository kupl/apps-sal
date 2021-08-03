class Solution:
    def knightDialer(self, n: int) -> int:
        space = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 7, 1], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}
        memory = {}
        if n < 1:
            return 0

        def recurse(number, n):
            if n < 2:
                return 1

            key = str([number, n])
            if key in memory:
                return memory[key]

            moves = 0
            for i in space[number]:
                moves += recurse(i, n - 1)

            memory[key] = moves
            return moves

        s = 0
        for number in space:
            s += recurse(number, n)

        return s % (10**9 + 7)
