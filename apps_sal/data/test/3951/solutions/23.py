"""
Author    : co_devil Chirag Garg
Institute : JIIT
"""
import itertools
import os
import sys
import threading
from collections import deque, Counter, OrderedDict, defaultdict
import heapq
from math import ceil, floor, log, sqrt, factorial, pow, pi, gcd
"from io import BytesIO, IOBase\nif sys.version_info[0] < 3:\n    from __builtin__ import xrange as range\n    from future_builtins import ascii, filter, hex, map, oct, zip\nelse:\n    from builtins import str as __str__\n    str = lambda x=b'': x if type(x) is bytes else __str__(x).encode()\nBUFSIZE = 8192\nclass FastIO(IOBase):\n    newlines = 0\n    def __init__(self, file):\n        self._buffer = BytesIO()\n        self._fd = file.fileno()\n        self._writable = 'x' in file.mode or 'r' not in file.mode\n        self.write = self._buffer.write if self._writable else None\n\n    def read(self):\n        return self._buffer.read() if self._buffer.tell() else os.read(self._fd, os.fstat(self._fd).st_size)\n\n    def readline(self):\n        while self.newlines == 0:\n            b, ptr = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE)), self._buffer.tell()\n            self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)\n            self.newlines += b.count(b'\n') + (not b)\n        self.newlines -= 1\n        return self._buffer.readline()\n\n    def flush(self):\n        if self._writable:\n            os.write(self._fd, self._buffer.getvalue())\n            self._buffer.truncate(0), self._buffer.seek(0)\nsys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)\ninput = lambda: sys.stdin.readline().rstrip(b'\r\n')\n\ndef print(*args, **kwargs):\n    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)\n    at_start = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop('end', b'\n'))\n    if kwargs.pop('flush', False):\n        file.flush()\n\n"


def ii():
    return int(input())


def si():
    return str(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod = 1000000007
(dx, dy) = ([-1, 1, 0, 0], [0, 0, 1, -1])


def getKey(item):
    return item[0]


def sort2(l):
    return sorted(l, key=getKey)


def d2(n, m, num):
    return [[num for x in range(m)] for y in range(n)]


def isPowerOfTwo(x):
    return x and (not x & x - 1)


def decimalToBinary(n):
    return bin(n).replace('0b', '')


def ntl(n):
    return [int(i) for i in str(n)]


def powerMod(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


graph = defaultdict(list)
visited = [0] * 1000000
col = [-1] * 1000000


def dfs(v, c):
    if visited[v]:
        if col[v] != c:
            print('-1')
            return
        return
    col[v] = c
    visited[v] = 1
    for i in graph[v]:
        dfs(i, c ^ 1)


def bfs(d, v):
    q = []
    q.append(v)
    visited[v] = 1
    while len(q) != 0:
        x = q[0]
        q.pop(0)
        for i in d[x]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)
        print(x)
    print(l)


def make_graph(e):
    d = {}
    for i in range(e):
        (x, y) = mi()
        if x not in list(d.keys()):
            d[x] = [y]
        else:
            d[x].append(y)
        if y not in list(d.keys()):
            d[y] = [x]
        else:
            d[y].append(x)
    return d


def gr2(n):
    d = {}
    for i in range(n):
        (x, y) = mi()
        if x not in list(d.keys()):
            d[x] = [y]
        else:
            d[x].append(y)
    return d


def connected_components(graph):
    seen = set()

    def dfs(v):
        vs = set([v])
        component = []
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
        return component
    ans = []
    for v in graph:
        if v not in seen:
            d = dfs(v)
            ans.append(d)
    return ans


ii()
(g, v) = (Counter(mi()), [])
while g:
    x = max(g)
    g[x] -= 1
    for y in v:
        g[gcd(x, y)] -= 2
    v.append(x)
    g += Counter()
print(' '.join(map(str, v)))
