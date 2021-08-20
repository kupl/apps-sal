from bisect import bisect_right
(A, B, Q) = list(map(int, input().split()))
INF = float('inf')
S = [-INF] + list((int(input()) for _ in range(A))) + [INF]
T = [-INF] + list((int(input()) for _ in range(B))) + [INF]
for _ in range(Q):
    x = int(input())
    i = bisect_right(S, x)
    j = bisect_right(T, x)
    d = INF
    for s in [S[i - 1], S[i]]:
        for t in [T[j - 1], T[j]]:
            d1 = abs(s - x) + abs(s - t)
            d2 = abs(t - x) + abs(s - t)
            d = min(d, d1, d2)
    print(d)
