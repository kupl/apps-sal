import sys
from functools import lru_cache

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def score(x, counter, N):
    ans = 0
    for i in range(40):
        if x & (1 << i):
            ans += (N - counter[i]) * (1 << i)
        else:
            ans += counter[i] * (1 << i)
    return ans


def main():
    N, K, *A = list(map(int, read().split()))

    counter = [0] * 40
    for a in A:
        for i in range(40):
            if a & (1 << i):
                counter[i] += 1

    B = [0] * 40
    for i in range(39):
        if counter[i] < N - counter[i]:
            B[i + 1] = B[i] + (1 << i)
        else:
            B[i + 1] = B[i]

    C = [0] * 40
    for i in range(39, 0, -1):
        if K & (1 << i):
            C[i - 1] = C[i] + (1 << i)
        else:
            C[i - 1] = C[i]

    ans = score(K, counter, N)

    for i in range(40):
        if K & (1 << i):
            x = B[i] + C[i]
            res = score(x, counter, N)
            if ans < res:
                ans = res

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
