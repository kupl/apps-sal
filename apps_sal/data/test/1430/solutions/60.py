import sys
from itertools import groupby, accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = list(map(int, readline().split()))
    S = readline().strip()

    vec = [len(list(g)) for _, g in groupby(S)]
    keys = [k for k, _ in groupby(S)]
    csum = [0]
    csum.extend(accumulate(vec))

    ans = 0
    for i in range(len(vec)):
        if keys[i] == '0':
            if i == 0:
                n = 2 * K
            else:
                continue
        else:
            n = 2 * K + 1

        if ans < csum[min(i + n, len(csum) - 1)] - csum[i]:
            ans = csum[min(i + n, len(csum) - 1)] - csum[i]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
