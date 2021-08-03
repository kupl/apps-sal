t = input()
n = len(t)
t = [-1] + [i for i in range(n - 1) if t[i] != t[i + 1]] + [n - 1]
n = len(t) - 1
u, v = [0] * n, [0] * n
for i in range(n):
    d = t[i + 1] - t[i]
    k = d // 2
    u[i] = v[i] = k
    if d & 1:
        if t[i] & 1:
            v[i] += 1
        else:
            u[i] += 1
    i += 1
a = sum(u[i] for i in range(0, n, 2))
b = sum(v[i] for i in range(0, n, 2))
c = sum(u[i] for i in range(1, n, 2))
d = sum(v[i] for i in range(1, n, 2))
print(a * b + c * d, (a * (a + 1) + b * (b + 1) + c * (c + 1) + d * (d + 1)) // 2)
