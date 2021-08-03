r, s, p = map(int, input().split())
n = 101
def g(i, j, k): return i + n * (j + n * k)


t = [0] * (n ** 3)
for i in range(1, n):
    for j in range(n):
        for k in range(n):
            l = g(i, j, k)
            if j or k:
                x, y, z = g(i, j - 1, k), g(i - 1, j, k), g(i, j, k - 1)
                a, b, c = i * j, i * k, j * k
                t[l] = (a * t[x] + b * t[y] + c * t[z]) / (a + b + c)
            else:
                t[l] = 1
x, y, z = g(r, s, p), g(s, p, r), g(p, r, s)
print(t[x], t[y], t[z])
