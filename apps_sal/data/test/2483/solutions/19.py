import sys
from itertools import accumulate
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, C, *STC) = list(map(int, read().split()))
    P = [[] for _ in range(C)]
    for (s, t, c) in zip(*[iter(STC)] * 3):
        P[c - 1].append((s, t))
    M = 10 ** 5
    vec = [0] * (M + 2)
    for i in range(C):
        P[i].sort()
        for (j, (s, t)) in enumerate(P[i]):
            if j > 0 and s == P[i][j - 1][1]:
                vec[s] += 1
                vec[t] += -1
            else:
                vec[s - 1] += 1
                vec[t] += -1
    vec = list(accumulate(vec))
    print(max(vec))
    return


def __starting_point():
    main()


__starting_point()
