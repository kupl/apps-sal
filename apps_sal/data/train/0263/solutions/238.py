class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        D = []
        modulo = 10 ** 9 + 7
        movesDict = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for i in range(10):
            D.append([-1] * (n + 1))

        def help(start, length):
            if length == 1:
                return 1
            if D[start][length] != -1:
                return D[start][length]
            moves = movesDict[start]
            total = 0
            for newStart in moves:
                total += help(newStart, length - 1)
                total %= modulo
            D[start][length] = total
            return total
        res = 0
        for i in range(10):
            res += help(i, n)
        return res % modulo


'\n1 -> 6, 8\n2 -> 7, 9\n3 -> 4, 8\n4 -> 3, 9, 0\n5 -> n/a\n6 -> 1, 7, 0\n7 -> 2, 6\n8 -> 1, 3\n9 -> 2, 4\ndp - solve how many for n - 1 starting at some index then ?\narray [start][length]\ninit with [10][n+1]\n\n\n\n'
