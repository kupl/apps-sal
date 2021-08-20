(n, k) = map(int, input().split())
v = list(range(1, 2 * n + 1))
for i in range(k):
    (v[2 * i], v[2 * i + 1]) = (v[2 * i + 1], v[2 * i])
print(' '.join(map(str, v)))
