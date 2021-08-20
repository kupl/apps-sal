def rd():
    return list(map(int, input().split()))


(n, m) = rd()
t = (n - 1) * n // 2
a = n - 1 >> 1
tt = a * (a + 1) + [a + 1, 0][n & 1]
r = 0
for i in range(m):
    (x, d) = rd()
    if d > 0:
        r += t * d + n * x
    else:
        r += tt * d + n * x
print(r / n)
