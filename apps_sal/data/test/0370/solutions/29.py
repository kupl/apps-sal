K = int(input())
(X, Y) = map(int, input().split())


def golf(a, b):
    if a < 0:
        t = golf(-a, b)
        return (-t[0], t[1])
    if b < 0:
        t = golf(a, -b)
        return (t[0], -t[1])
    if a > b:
        t = golf(b, a)
        return (t[1], t[0])
    if a + b >= K * 2:
        return (a, b - K)
    if a + b == K:
        return (0, 0)
    r = K - (a + b) // 2
    return (-r, a + b + r - K)


if K % 2 == 0 and (X + Y) % 2 == 1:
    print(-1)
else:
    res = []
    while X or Y:
        res.append((X, Y))
        (X, Y) = golf(X, Y)
    print(len(res))
    for r in res[::-1]:
        print(r[0], r[1])
