import bisect
(a, b, q) = list(map(int, input().split()))
INF = 10 ** 18
shrines = [-INF] + [int(input()) for _ in range(a)]
temples = [-INF] + [int(input()) for _ in range(b)]
for _ in range(q):
    x = int(input())
    ans = INF
    Ri = bisect.bisect_left(shrines, x)
    Li = Ri - 1
    if Ri != a + 1:
        R = shrines[Ri]
        Rj = bisect.bisect_left(temples, R)
        Lj = Rj - 1
        d = INF
        if Rj != b + 1:
            d = min(d, temples[Rj] - x)
        if Lj != 0:
            d = min(d, R - temples[Lj] + R - x)
        if d < ans:
            ans = d
    if Li != 0:
        L = shrines[Li]
        Rj = bisect.bisect_left(temples, L)
        Lj = Rj - 1
        d = INF
        if Rj != b + 1:
            d = min(d, temples[Rj] - L + x - L)
        if Lj != 0:
            d = min(d, x - temples[Lj])
        if d < ans:
            ans = d
    Ri = bisect.bisect_left(temples, x)
    Li = Ri - 1
    if Ri != b + 1:
        R = temples[Ri]
        Rj = bisect.bisect_left(shrines, R)
        Lj = Rj - 1
        d = INF
        if Rj != a + 1:
            d = min(d, shrines[Rj] - x)
        if Lj != 0:
            d = min(d, R - shrines[Lj] + R - x)
        if d < ans:
            ans = d
    if Li != 0:
        L = temples[Li]
        Rj = bisect.bisect_left(shrines, L)
        Lj = Rj - 1
        d = INF
        if Rj != a + 1:
            d = min(d, shrines[Rj] - L + x - L)
        if Lj != 0:
            d = min(d, x - shrines[Lj])
        if d < ans:
            ans = d
    print(ans)
