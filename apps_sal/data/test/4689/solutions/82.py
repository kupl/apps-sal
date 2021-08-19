(k, n) = map(int, input().split())
a = list(map(int, input().split()))
ans = k
mx = k - a[-1] + a[0]
for i in range(n - 1):
    mx = max(mx, abs(a[i] - a[i + 1]))
print(ans - mx)
