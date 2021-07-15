import sys
from itertools import groupby

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    idx = 0
    ans = [0] * len(S)
    for k, g in groupby(S):
        L = len(list(g))
        if k == 'R':
            for i in range(L):
                if (L - i) % 2 == 0:
                    ans[idx + L] += 1
                else:
                    ans[idx + L - 1] += 1
        if k == 'L':
            for i in range(L):
                if i % 2 == 0:
                    ans[idx] += 1
                else:
                    ans[idx - 1] += 1

        idx += L

    print((*ans))
    return


def __starting_point():
    main()

__starting_point()
