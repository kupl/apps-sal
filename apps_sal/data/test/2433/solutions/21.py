t = int(input())
for _ in range(t):
    (b, p, f) = list(map(int, input().split()))
    (h, c) = list(map(int, input().split()))
    b //= 2
    if h < c:
        (p, f) = (f, p)
        (h, c) = (c, h)
    p = min(b, p)
    b -= p
    f = min(b, f)
    print(p * h + f * c)
