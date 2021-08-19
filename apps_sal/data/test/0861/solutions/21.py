(m, r) = list(map(int, input().split()))
(res, sq2) = (0, 2 ** 0.5)
for i in range(1, m):
    res += 2 + sq2 + 2 * sq2 * (i - 1) + (i - 1) * i
res = (res + m) * 2 * r
print(res / (m * m))
