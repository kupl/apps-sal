T = int(input())
for t in range(T):
    (a, b, c) = sorted(map(int, input().strip().split()))
    d = c - b
    v = a
    if d > a:
        v += min(c - a, b)
    else:
        a -= d
        c -= d + a // 2
        b -= a - a // 2
        v += min(c, b)
    print(v)
