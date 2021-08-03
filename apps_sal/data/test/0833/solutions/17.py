def R(): return list(map(int, input().split()))


n, v = R()
M = 3005
x = [0] * M
for i in range(n):
    a, b = R()
    x[a - 1] += b
y = [0] * M
s = 0
for i in range(M):
    a = min(v, y[i])
    b = min(v - a, x[i])
    s += a + b
    if i < M - 1:
        y[i + 1] = x[i] - b
print(s)
