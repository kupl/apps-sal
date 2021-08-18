from collections import deque
import sys
try:
    from typing import Deque, List
except ImportError:
    pass


def solve(K: int):
    pars = list(range(K))

    def union(a: int, b: int):
        pars[a] = b

    def getpar(a: int):
        if pars[a] == a:
            return a
        pars[a] = getpar(pars[a])
        return pars[a]

    for i in range(K):
        union(getpar(i), getpar(i * 10 % K))

    gs = [getpar(i) for i in range(K)]
    if gs[0] == gs[1]:
        print((1))
        return
    G = [[] for i in range(K)]
    for i in range(K):
        G[gs[i]].append(gs[(i + 1) % K])
    d = {gs[1]: 1}
    q = deque()
    q.append(gs[1])
    while q:
        s = q.popleft()
        for t in G[s]:
            if t in d:
                continue
            d[t] = d[s] + 1
            if t == gs[0]:
                print((d[t]))
                return
            q.append(t)
    assert False


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))
    solve(K)


def __starting_point():
    main()


__starting_point()
