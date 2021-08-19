from itertools import accumulate, chain


class Fenwick:

    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    def get(self, i):
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total


def solution(n, a, t):
    S = [s for s in accumulate(a)]
    T = [[s, s - t] for s in S]
    T = list(set(chain(*T)))
    T.sort()
    T = {v: i for (i, v) in enumerate(T)}
    fenwick = Fenwick(len(T))
    total = 0
    for (i, v) in enumerate(S):
        diff = v - t
        total += i - fenwick.get(T[diff])
        if v < t:
            total += 1
        fenwick.update(T[v], 1)
    return total


def f():
    return [int(c) for c in input().split()]


(n, t) = f()
a = f()
print(solution(n, a, t))
