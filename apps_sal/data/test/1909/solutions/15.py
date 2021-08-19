(n, k) = map(int, input().split())
xs = list(map(int, input().split()))
res = (10 ** 9, -1)
for i in range(k):
    s = 0
    for j in range(i, n, k):
        s += xs[j]
    res = min(res, (s, i + 1))
print(res[1])
