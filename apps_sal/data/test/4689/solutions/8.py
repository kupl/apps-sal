k, n = list(map(int, input().split()))
a = list(map(int, input().split()))
mx = a[0] + k - a[n - 1]
for i in range(n - 1):
    mx = max(mx, a[i + 1] - a[i])
print((k - mx))

