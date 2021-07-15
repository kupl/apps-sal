n, b, p = map(int, input().split())
c, v = n, 0
while c > 1:
    k = 2
    while 2 * k <= c:
        k *= 2
    c -= k // 2
    v += k * b + k // 2
print(v, n * p)
