(n, k) = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(min(n, k) + 1):
    for j in range(min(n, k) - i + 1):
        lis = sorted(v[:i] + v[n - j:])
        for l in range(k - i - j + 1):
            ans = max(ans, sum(lis[l:]))
print(ans)
