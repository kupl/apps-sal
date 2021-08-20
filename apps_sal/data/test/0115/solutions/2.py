(r, s, p) = map(int, input().split())
n = 101
m = n * n
t = [0] * n * m
for i in range(1, n):
    for j in range(n):
        for k in range(n):
            d = i + n * j + m * k
            a = i * j * t[d - n] + i * k * t[d - 1] + j * k * t[d - m]
            b = i * j + i * k + j * k
            t[d] = a / b if j or k else 1
print(t[r + n * s + m * p], t[s + n * p + m * r], t[p + n * r + m * s])
