from heapq import heappush, heappop
from collections import deque
import sys
sys.setrecursionlimit(10000)


class Memoize:

    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


class Recurse(Exception):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):

    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated


(n, m) = list(map(int, input().split()))
d = sorted(map(int, input().split()))
(g, r) = list(map(int, input().split()))
q = deque([(0, 0, g)])
cost = [[-1] * (g + 1) for _ in range(m)]
while len(q):
    (c, x, t) = q.popleft()
    if cost[x][t] != -1:
        continue
    cost[x][t] = c
    back = False
    if t == 0:
        back = True
        c += r
        t = g
    for di in [-1, 1]:
        ni = x + di
        if ni >= 0 and ni < m:
            step = abs(d[x] - d[ni])
            if step <= t:
                if back:
                    q.append((c + step, ni, t - step))
                else:
                    q.appendleft((c + step, ni, t - step))
res = list([x for x in cost[m - 1] if x != -1])
print(min(res) if len(res) else -1)
