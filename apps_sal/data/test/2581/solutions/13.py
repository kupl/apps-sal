import os
import sys
from math import *
from collections import *
from bisect import *
from io import BytesIO, IOBase


def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
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


class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def input():
    return sys.stdin.readline().rstrip('\r\n')


ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 10 ** 9 + 7
EPS = 1e-06


def Ceil(a, b):
    return a // b + int(a % b > 0)


def value():
    return tuple(map(int, input().split()))


def array():
    return [int(i) for i in input().split()]


def Int():
    return int(input())


def Str():
    return input()


def arrayS():
    return [i for i in input().split()]


n = Int()
a = []
for i in range(n):
    a.append(array())
left = defaultdict(int)
right = defaultdict(int)
for i in range(n):
    for j in range(n):
        left[i - j] += a[i][j]
        right[i - (n - j - 1)] += a[i][j]
ans1 = (-1, -1, -1)
ans2 = (-1, -1, -1)
for i in range(n):
    for j in range(n):
        left_key = i - j
        right_key = i - (n - j - 1)
        here = (left[left_key] + right[right_key] - a[i][j], i + 1, j + 1)
        if n % 2 and left_key % 2 == right_key % 2:
            if left_key % 2:
                ans1 = max(ans1, here)
            else:
                ans2 = max(ans2, here)
        elif n % 2 == 0 and left_key % 2 != right_key % 2:
            if left_key % 2:
                ans1 = max(ans1, here)
            else:
                ans2 = max(ans2, here)
print(ans1[0] + ans2[0])
print(*ans1[1:], *ans2[1:])
