import cmath
import operator
import re
import copy
import os
import io
import sys
from builtins import *
from collections import Counter, defaultdict
from functools import reduce, lru_cache
from itertools import *
from bisect import *
from heapq import *
from math import *


def main():
    for _ in inputt(1):
        (n,) = inputi()
        if n <= 2:
            print(-1)
            continue
        A = [[0] * n for i in range(n)]
        yie = count(1)
        for a in range(n - 3):
            for b in range(a, n)[::-1]:
                A[a][b] = next(yie)
            for b in range(a + 1, n)[::-1]:
                A[b][a] = next(yie)
        A[n - 3][n - 3] = next(yie)
        A[n - 3][n - 2] = next(yie)
        A[n - 1][n - 2] = next(yie)
        A[n - 1][n - 3] = next(yie)
        A[n - 2][n - 2] = next(yie)
        A[n - 2][n - 1] = next(yie)
        A[n - 3][n - 1] = next(yie)
        A[n - 2][n - 3] = next(yie)
        A[n - 1][n - 1] = next(yie)
        for a in A:
            print(*a)


BUFSIZE = 8192


class FastIO(io.IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = io.BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            (self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr))
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            (self.buffer.truncate(0), self.buffer.seek(0))


class IOWrapper(io.IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


def print(*args, **kwargs):
    for x in args:
        file.write(str(x))
    file.write(kwargs.pop('end', '\n'))


(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def input():
    return sys.stdin.readline().rstrip('\r\n')


def inputt(t=0):
    return range(t) if t else range(int(input()))


def inputi():
    return map(int, input().split())


def inputl():
    return list(inputi())


def __starting_point():
    main()


__starting_point()
