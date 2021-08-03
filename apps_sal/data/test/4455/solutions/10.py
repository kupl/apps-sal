def R(): return map(int, input().split())


n, k = R()

r = list(R())
h = sorted(r)
d = {}

d[h[0]] = 0  # d[i]: 比i小的数字数量
for i in range(1, n):
    if h[i - 1] != h[i]:
        d[h[i]] = i

res = [0] * n
for i in range(n):
    res[i] = d[r[i]]

for i in range(k):
    a, b = R()
    a -= 1
    b -= 1
    if r[a] > r[b]:
        res[a] -= 1
    elif r[a] < r[b]:
        res[b] -= 1

res = list(map(str, res))
print(' '.join(res))
