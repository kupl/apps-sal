import datetime
import sys
import copy
import functools
import collections
import itertools


class Solution:

    def __init__(self):
        self.N = 0
        self.boards = None

    def test(self):
        pass

    def readInput(self):
        self.N = int(input())
        self.boards = []
        for i in range(self.N):
            self.boards.append(list(input()))

    def readMockInput(self):
        pass

    def solve(self):
        N = self.N
        impossibleMoves = set()
        chesses = list()
        notAttacked = list()
        for r in range(N):
            for c in range(N):
                if self.boards[r][c] == 'o':
                    chesses.append((r, c))
                elif self.boards[r][c] == '.':
                    notAttacked.append((r, c))
        for (r, c) in chesses:
            for (i, j) in notAttacked:
                impossibleMoves.add((i - r, j - c))
        startTime = datetime.datetime.now()
        for i in range(N):
            for j in range(N):
                if self.boards[i][j] == 'o':
                    continue
                for (r, c) in chesses:
                    if (i - r, j - c) not in impossibleMoves:
                        if self.boards[i][j] == '.':
                            print('NO')
                            return
                        self.boards[i][j] = 'v'
        if sum([row.count('x') for row in self.boards]) > 0:
            print('NO')
            return
        sys.stderr.write('Check Cost: {}\n'.format(datetime.datetime.now() - startTime))
        rn = 2 * N - 1
        res = [['.' for c in range(rn)] for r in range(rn)]
        res[N - 1][N - 1] = 'o'
        for i in range(-N + 1, N):
            for j in range(-N + 1, N):
                if not (i == 0 and j == 0) and (i, j) not in impossibleMoves:
                    res[i + N - 1][j + N - 1] = 'x'
        print('YES')
        for row in res:
            print(''.join(row))


solution = Solution()
solution.readInput()
startTime = datetime.datetime.now()
solution.solve()
sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))
