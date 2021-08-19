from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N = int(input())
XD = [[int(i) for i in input().split()] for _ in range(N)]
XD.sort()
MOD = 998244353


def make():
    edge = [[] for _ in range(N)]
    parent = [-1] * N
    MAXIDX = N
    sorted_X = [X for (X, _) in XD]
    for i in range(N - 1, -1, -1):
        idx = bisect_left(sorted_X, XD[i][0] + XD[i][1])
        for j in range(i + 1, min(idx, MAXIDX)):
            if parent[j] < 0:
                parent[j] = i
        if idx >= MAXIDX:
            MAXIDX = i + 1
    for (i, par) in enumerate(parent):
        if par < 0:
            continue
        edge[par].append(i)
    return (parent, edge)


(parent, edge) = make()


def cnt(node):
    if not edge[node]:
        return 2
    res = 1
    for v in edge[node]:
        res = res * cnt(v) % MOD
    res += 1
    return res % MOD


def main():
    ans = 1
    for (i, par) in enumerate(parent):
        if par < 0:
            ans = ans * cnt(i) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
