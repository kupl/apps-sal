import bisect
A, B, Q = list(map(int, input().split()))
INF = float('inf')
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

for q in range(Q):
    x = int(input())
    b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
    res = INF
    for S in [s[b - 1], s[b]]:
        for T in [t[d - 1], t[d]]:
            d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
            res = min(res, d1, d2)
    print(res)
