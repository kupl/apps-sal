(nim, mike, kite) = map(int, input().split())
H = [int(input()) for _ in range(nim)]
C = mike - kite
(l, r) = (0, 1 << 30)
while r - l > 1:
    m = (l + r) // 2
    if sum([max((h - kite * m + C - 1) // C, 0) for h in H]) <= m:
        r = m
    else:
        l = m
print(r)
