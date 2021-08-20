(m, n) = map(int, input().split())
mx = 0
for i in range(n):
    (a, b) = map(int, input().split())
    mx += a * m
    if b > 0:
        mx += b * (m - 1) * m // 2
    elif m % 2 == 1:
        k = m // 2 + 1
        mx += b * (k - 1) * k
    else:
        k = m // 2
        mx += b * k * k
print(mx / m)
