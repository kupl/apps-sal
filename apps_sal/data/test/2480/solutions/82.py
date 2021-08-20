import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def solve():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    S = [0 for _ in range(N + 1)]
    for i in range(N):
        S[i + 1] = S[i] + A[i] - 1
    d = dict()
    for i in range(N + 1):
        k = S[i] % K
        if k in d:
            d[k].append(i)
        else:
            d[k] = [i]
    ans = 0
    for (k, v) in list(d.items()):
        if len(v) <= 1:
            continue
        else:
            for i in range(len(v)):
                s = v[i] + K - 1
                si = bisect.bisect_right(v, s)
                ans += si - i - 1
    print(ans)


def __starting_point():
    solve()


__starting_point()
