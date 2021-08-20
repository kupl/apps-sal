import sys
for _ in range(int(input())):
    (n, d) = map(int, input().split())
    res = d
    for a in range(int(d ** 0.5) - 10, int(d ** 0.5) + 10):
        if a < 0:
            continue
        res = min(res, a + (d + a) // (a + 1))
    if res <= n:
        print('YES')
    else:
        print('NO')
