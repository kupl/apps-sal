from bisect import bisect_right
import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)


def main():
    n, w = map(int, input().split())
    minw, u = map(int, input().split())
    item = {minw: [u], minw + 1: [], minw + 2: [], minw + 3: []}
    for _ in range(n - 1):
        wei, u = map(int, input().split())
        item[wei].append(u)

    l = [0] * 4
    keys = sorted(item.keys())
    i = 0
    for k in keys:
        item[k].sort(reverse=True)
        l[i] = len(item[k])
        i += 1

    X = set()
    for i in range(l[0] + 1):
        if i == 0:
            cumsum = 0
        else:
            cumsum += item[minw][i - 1]
        cumsumx = cumsum
        for j in range(l[1] + 1):
            weight = minw * i + (minw + 1) * j
            if j != 0:
                cumsumx += item[minw + 1][j - 1]
            if weight <= w:
                X.add((weight, cumsumx))

    Y = []
    for i in range(l[2] + 1):
        if i == 0:
            cumsum = 0
        else:
            cumsum += item[minw + 2][i - 1]
        cumsumy = cumsum
        for j in range(l[3] + 1):
            weight = (minw + 2) * i + (minw + 3) * j
            if j != 0:
                cumsumy += item[minw + 3][j - 1]
            if weight <= w:
                Y.append((weight, cumsumy))

    Y.sort(key=lambda x: x[0])
    Yw = [0] * len(Y)
    cummax = [0] * len(Y)
    for i in range(len(Y)):
        if i == 0:
            cummax[i] = Y[i][1]
            Yw[i] = Y[i][0]
        else:
            cummax[i] = max(cummax[i - 1], Y[i][1])
            Yw[i] = Y[i][0]

    ans = 0
    for x in X:
        wei, va = x
        idx = bisect_right(Yw, w - wei)
        if idx == 0:
            continue
        else:
            ans = max(ans, cummax[idx - 1] + va)

    print(ans)


def __starting_point():
    main()


__starting_point()
