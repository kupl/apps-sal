'''
Name: Devansh
Username: singhdevansh
Github: https://github.com/Devansh3712
'''

import os
import sys
import math
from itertools import *
from io import BytesIO, IOBase
from collections import *

# <fast I/O>
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
# </fast I/O>

# <template>
mod = (10**9) + 7
pi = 3.14159265358979323846264338327950


def i1():  # int(input())
    return int(sys.stdin.readline())


def sf():  # input()
    return sys.stdin.readline()


def mi():  # map(int(input()))
    return map(int, sys.stdin.readline().split())


def arr():  # list(map(int,input().split()))
    return list(map(int, sys.stdin.readline().split()))


def pf(ans):  # print(x)
    return sys.stdout.write(str(ans) + "\n")


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def LogN(a, b):
    return math.log(a) / math.log(b)


def fpow(a, b):
    res = 1
    while (b > 0):
        if b & 1:
            res = res * a
        a = a * a
        b >>= 1
    return res


def sieve(n):
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:
            ps.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1
        p += 2
    return ps
# </template>

# <solve>


def solve():
    n = i1()
    l1 = arr()
    l2 = arr()
    ans = []
    for i in range(n):
        c = 0
        for j in range(i + 1):
            if l1[j] <= l2[i]:
                c += l1[j]
                l1[j] = 0
            else:
                l1[j] -= l2[i]
                c += l2[i]
        ans.append(c)
    print(*ans)


solve()
# </solve>

# <solution>
# tc=i1()
# for t in range (tc):
# 	solve()
# <solution>
