import sys
from bisect import bisect_left
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (A, B, Q) = list(map(int, readline().split()))
    S = [-INF]
    S.extend((int(readline()) for _ in range(A)))
    S.append(INF)
    T = [-INF]
    T.extend((int(readline()) for _ in range(B)))
    T.append(INF)
    X = [int(readline()) for _ in range(Q)]
    ans = [INF] * Q
    for (i, x) in enumerate(X):
        i1 = bisect_left(S, x)
        i2 = bisect_left(T, x)
        ans[i] = min(abs(x - S[i1 - 1]) + abs(S[i1 - 1] - T[i2 - 1]), abs(x - T[i2 - 1]) + abs(T[i2 - 1] - S[i1 - 1]), abs(x - S[i1 - 1]) + abs(S[i1 - 1] - T[i2]), abs(x - T[i2 - 1]) + abs(T[i2 - 1] - S[i1]), abs(x - S[i1]) + abs(S[i1] - T[i2]), abs(x - T[i2]) + abs(T[i2] - S[i1]), abs(x - S[i1]) + abs(S[i1] - T[i2 - 1]), abs(x - T[i2]) + abs(T[i2] - S[i1 - 1]))
    print('\n'.join(map(str, ans)))
    return


def __starting_point():
    main()


__starting_point()
