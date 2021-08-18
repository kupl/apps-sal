from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, D, A = list(map(int, input().split()))
    XH = [None] * N
    X = [None] * N

    for i in range(N):
        XH[i] = tuple(map(int, input().split()))
        X[i] = XH[i][0]

    XH.sort()
    X.sort()

    ans = 0
    S = [0] * (N + 1)
    for i in range(N):
        if S[i] < XH[i][1]:
            need = (XH[i][1] - S[i] + A - 1) // A
            j = bisect_right(X, X[i] + 2 * D)
            S[i] += need * A
            S[j] -= need * A
            ans += need
        S[i + 1] += S[i]
    print(ans)


def __starting_point():
    main()


__starting_point()
