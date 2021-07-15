n, m = map(int, input().split())
t, p = [m] * n, list(map(int, input().split()))
for i, j in enumerate(p):
    if t[j - 1] == m: t[j - 1] = i
for i in range(n - 1): t[i + 1] = min(t[i], t[i + 1])
for i in range(n): t[i] = p[t[i]]
print(' '.join(map(str, t)))
