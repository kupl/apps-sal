import sys
import os
import math
import array
3


def main():
    (N, M) = read_ints()
    X = [x - 1 for x in read_ints()]
    print(*solve(N, M, X))


def solve(N, M, X):
    pos = list(range(N))
    pairs = [dict() for _ in range(N)]
    fsum = 0
    for i in range(M - 1):
        a = X[i]
        b = X[i + 1]
        if a == b:
            continue
        if b not in pairs[a]:
            pairs[a][b] = 0
        if a not in pairs[b]:
            pairs[b][a] = 0
        pairs[a][b] += 1
        pairs[b][a] += 1
        fsum += abs(pos[a] - pos[b])
    ans = [fsum]
    fst = 0
    for i in range(N - 1):
        j = i + 1
        pi = pos[i]
        pj = pos[j]
        d = 0
        for (k, c) in pairs[i].items():
            if k == j:
                continue
            pk = pos[k]
            d -= abs(pi - pk) * c
            d += abs(pj - pk) * c
        for (k, c) in pairs[j].items():
            if k == i:
                continue
            pk = pos[k]
            d -= abs(pj - pk) * c
            d += abs(pi - pk) * c
        fsum += d
        ans.append(fsum)
        (pos[i], pos[j]) = (pj, pi)
    return ans


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
