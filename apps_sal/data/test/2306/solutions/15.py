n, *L = map(int, open(0).read().split())
T, V = L[:n], L[n:]
s = sum(T)
a = [0]
for t, v1, v2 in zip(T, V, V[1:] + [0]):
    a += [v1] * (2 * t - 1) + [min(v1, v2)]
for i in range(2 * s):
    a[i + 1] = min(a[i + 1], a[i] + .5)
for i in range(2 * s, 0, -1):
    a[i - 1] = min(a[i - 1], a[i] + .5)
print(sum(a) / 2)
