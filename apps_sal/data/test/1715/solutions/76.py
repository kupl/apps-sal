import bisect

A, B, Q = list(map(int, input().split()))
INF = 10**18
S = [-INF] + [int(input()) for i in range(A)] + [INF]
T = [-INF] + [int(input()) for i in range(B)] + [INF]
X = [int(input()) for i in range(Q)]


for x in X:
    d = float("inf")
    i = bisect.bisect_right(S, x)
    j = bisect.bisect_right(T, x)
    for s in [S[i - 1], S[i]]:
        for t in [T[j - 1], T[j]]:
            d1 = abs(s - x) + abs(t - s)
            d2 = abs(t - x) + abs(t - s)
            d = min(d, d1, d2)
    print(d)
