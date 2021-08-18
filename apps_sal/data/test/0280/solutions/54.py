import sys
input = sys.stdin.readline


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


def main():
    mod = 10**9 + 7
    inf = 10**10

    N, M = MI()
    W = LI()
    LV = [[0, 0] for _ in range(M)]
    mV = inf
    for i in range(M):
        LV[i][0], LV[i][1] = MI()
        mV = min(mV, LV[i][1])

    if max(W) > mV:
        print((-1))
        return

    LV.sort(reverse=True)
    nVL = [(0, 0)]

    MV = inf
    for i in range(M):
        l, v = LV[i]
        if v < MV:
            nVL.append((v, l))
            MV = v

    nVL.sort()

    from collections import defaultdict
    dd = defaultdict(int)

    import bisect

    def calc(x):

        if dd[x]:
            return dd[x]

        temp = (x, -1)
        num = bisect.bisect_left(nVL, temp) - 1

        v, l = nVL[num]
        dd[x] = l
        return l

    import itertools

    ans = inf

    for ite in itertools.permutations(list(range(N)), N):
        Cs = []
        for i in ite:
            Cs.append(W[i])

        S = [0] * (N + 1)
        for i in range(N):
            S[i + 1] = S[i] + Cs[i]

        X = [0] * N

        for i in range(N):
            for j in range(i + 1, N):
                w = S[j + 1] - S[i]
                l = calc(w)
                X[j] = max(X[j],
                           X[i] + l)

        temp = X[-1]
        ans = min(ans, temp)

    print(ans)


main()
