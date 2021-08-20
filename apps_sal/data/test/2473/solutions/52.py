(n, k, *L) = map(int, open(0).read().split())
X = []
Y = []
for (x, y) in sorted(((x, y) for (x, y) in zip(*[iter(L)] * 2))):
    X.append(x)
    Y.append(y)
ans = float('inf')
for i in range(n - k + 1):
    for j in range(i + k - 1, n):
        w = X[j] - X[i]
        l = sorted(Y[i:j + 1])
        h = min((My - my for (my, My) in zip(l, l[k - 1:])))
        ans = min(ans, w * h)
print(ans)
