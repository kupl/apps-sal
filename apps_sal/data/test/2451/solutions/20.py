(n, h, a, b, k) = map(int, input().split())
for i in range(k):
    num = 0
    (p, q, r, s) = map(int, input().split())
    if p == r:
        num = abs(q - s)
    elif a <= q <= b:
        num += abs(p - r)
        num += abs(q - s)
    elif b < q:
        num += q - b
        num += abs(p - r)
        num += abs(b - s)
    else:
        num += a - q
        num += abs(p - r)
        num += abs(a - s)
    print(num)
