

import os
import sys
from io import BytesIO, IOBase
from math import inf


def main():
    # a bishop has to be on a cell intercepted by even diagonals,
    # and another on a cell intercepted by odd diagonals

    # i + j is even -> white
    # i + j is odd -> gray

    # diagonal 1 -> i - j (top-left to bottom-right) (this difference is constant)
    # diagonal 2 -> i + j (top-right to bottom-left) (this sum is constant)

    # calculate the sum of each diagonal (n2)

    # find the best cell (with max total) intercepted by even diagonals and the
    # best cell (with max total) intercepted by odd diagonals

    n = int(input())
    chessboard = [
        [int(x) for x in input().split()]
        for row in range(n)
    ]

    mainDiagonalSums = {}
    secondaryDiagonalSums = {}

    for i in range(n):
        for j in range(n):
            mainDiagonal = i - j
            if mainDiagonal in mainDiagonalSums:
                mainDiagonalSums[mainDiagonal] += chessboard[i][j]
            else:
                mainDiagonalSums[mainDiagonal] = chessboard[i][j]

            secondaryDiagonal = i + j
            if secondaryDiagonal in secondaryDiagonalSums:
                secondaryDiagonalSums[secondaryDiagonal] += chessboard[i][j]
            else:
                secondaryDiagonalSums[secondaryDiagonal] = chessboard[i][j]

    maxPoints = [-inf, -inf]
    bestPosition = [None, None]

    for i in range(n):
        for j in range(n):
            points = (
                mainDiagonalSums[i - j] + secondaryDiagonalSums[i + j] -
                chessboard[i][j]
            )

            if (i + j) & 1:
                if points > maxPoints[1]:
                    bestPosition[1] = (i, j)
                    maxPoints[1] = points
            else:
                if points > maxPoints[0]:
                    bestPosition[0] = (i, j)
                    maxPoints[0] = points

    print(sum(maxPoints))
    print(' '.join([f'{i+1} {j+1}' for i, j in bestPosition]))


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


input = lambda: sys.stdin.readline().rstrip("\r\n")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep = kwargs.pop("sep", " ")
    file = kwargs.pop("file", sys.stdout)

    atStart = True
    for x in args:
        if not atStart:
            file.write(sep)
        file.write(str(x))
        atStart = False
    file.write(kwargs.pop("end", "\n"))

    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

main()
