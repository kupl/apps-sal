import sys
from collections import defaultdict

INF = float("inf")


def solve(N: int, X: int, D: int):
    if D == 0:
        if X == 0:
            print((1))
        else:
            print((N + 1))
        return

    if D < 0:
        X = X + (N - 1) * D
        D = abs(D)

    segs = defaultdict(list)
    for k in range(N + 1):
        L = k * (k - 1) // 2
        R = k * N - k * (k + 1) // 2
        Ck = k * X + D * L
        Rk = R - L
        seg = (Ck // D, Ck // D + Rk + 1)
        s = Ck % D
        segs[s].append(seg)

    tot = 0
    for k in segs:
        event = defaultdict(int)
        for l, r in segs[k]:
            event[l] += 1
            event[r] -= 1

        curr = 0
        pre = -1
        for k in sorted(event.keys()):
            if curr > 0:
                tot += k - pre
            curr += event[k]
            pre = k
    print(tot)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    X = int(next(tokens))
    D = int(next(tokens))
    solve(N, X, D)


def __starting_point():
    main()


__starting_point()
