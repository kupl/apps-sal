import sys
import os
3


def main():
    T = read_int()
    for _ in range(T):
        N = read_int()
        A = read_ints()
        M = read_int()
        H = [tuple(read_ints()) for _ in range(M)]
        print(solve(N, A, M, H))


def solve(N, A, M, H):
    H.sort(key=lambda h: (h[1], -h[0]))
    spow = [0] * (N + 1)
    s0 = 0
    for (p, s) in H:
        if s0 == s:
            continue
        spow[s] = p
        s0 = s
    maxp = 0
    for d in range(N, -1, -1):
        maxp = max(maxp, spow[d])
        spow[d] = maxp
    ans = 0
    maxa = A[0]
    if A[0] > spow[1]:
        return -1
    start = 0
    for (i, a) in enumerate(A[1:]):
        if a > spow[1]:
            return -1
        i += 1
        days = i - start + 1
        maxa = max(maxa, a)
        if spow[days] < maxa:
            ans += 1
            maxa = a
            start = i
    return ans + 1


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
