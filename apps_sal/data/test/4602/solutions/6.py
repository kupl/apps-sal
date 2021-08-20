(N, K, *X) = map(int, open(0).read().split())
ans = 0
for (y, x) in enumerate(X, start=1):
    a = x * 2
    b = (K - x) * 2
    ans += min(a, b)
print(ans)
