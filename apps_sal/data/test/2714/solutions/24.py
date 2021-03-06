from __future__ import division, print_function
import sys
import os
from io import IOBase, BytesIO
from types import GeneratorType


def bootstrap(f, stack=[]):

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


mod = 998244353


def power(base, exp):
    base %= mod
    if exp < 3:
        return base ** exp % mod
    half = power(base * base, exp // 2)
    return half * base % mod if exp % 2 == 1 else half % mod


def solve():
    (n, m) = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    (count, visited) = ([0, 0], [-1 for _ in range(n + 1)])
    for _ in range(m):
        (u, v) = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    (possible, ans) = (True, 1)

    @bootstrap
    def dfs(node, par, parity):
        nonlocal possible, visited, graph, count
        if visited[node] != -1:
            possible = False if visited[node] != parity else possible
            yield None
        visited[node] = parity
        count[parity] += 1
        for child in graph[node]:
            if child != par:
                yield dfs(child, node, 1 - parity)
        yield
    for i in range(1, n + 1):
        if visited[i] == -1:
            count = [0, 0]
            dfs(i, -1, 1)
            ans *= (power(2, count[0]) + power(2, count[1])) % mod
            ans %= mod
    sys.stdout.write(str(ans) if possible else '0')
    sys.stdout.write('\n')


def main():
    tests = 1
    tests = int(input().strip())
    for test in range(tests):
        solve()


py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
BUFSIZE = 8192


class FastIO(BytesIO):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = 'x' in file.mode or 'w' in file.mode
        self.write = super(FastIO, self).write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0, 2), super(FastIO, self).write(s))[0])
        return s

    def read(self):
        while self._fill():
            pass
        return super(FastIO, self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill()
            self.newlines = s.count(b'\n') + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            (self.truncate(0), self.seek(0))


class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s: self.buffer.write(s.encode('ascii'))
            self.read = lambda: self.buffer.read().decode('ascii')
            self.readline = lambda: self.buffer.readline().decode('ascii')


(sys.stdin, sys.stdout) = (IOWrapper(sys.stdin), IOWrapper(sys.stdout))


def input():
    return sys.stdin.readline().rstrip('\r\n')


main()
