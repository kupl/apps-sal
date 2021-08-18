
import os
from io import BytesIO, IOBase
import sys
from collections import defaultdict, deque, Counter
from bisect import *
from math import sqrt, pi, ceil, log
import math
from itertools import permutations
from copy import deepcopy

from sys import setrecursionlimit


def main():
    a = input().rstrip()
    n = len(a)
    a = Counter(a)
    a["6"] -= 1
    a["1"] -= 1
    a["8"] -= 1
    a["9"] -= 1
    z, s, y = 0, [], [1]
    for i in range(n):
        y.append((y[-1] * 10) % 7)
    xx = 1
    for i in a:
        if i != "0":
            x = int(i)
            for j in range(a[i]):
                s.append(i)
                z = (z + x * y[n - xx]) % 7
                xx += 1
    f = 1
    for i in permutations([1, 6, 8, 9]):
        if (z + i[0] * y[n - xx] + i[1] * y[n - xx - 1] + i[2] * y[n - xx - 2] + i[3] * (y[n - xx - 3])) % 7 == 0:
            f = 0
            s.extend([str(i[0]), str(i[1]), str(i[2]), str(i[3])])
            break
    if f:
        print(0)
    else:
        s.append("0" * a["0"])
        print("".join(s))


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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")


def __starting_point():
    main()


__starting_point()
