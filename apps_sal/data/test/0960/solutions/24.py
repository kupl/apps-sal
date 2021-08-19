(n, k) = map(int, input().split())
a = []
for i in range(1, min(int(n ** 0.5) + 1, k)):
    if n % i == 0:
        a.append((i, n // i))
ans = int(10000000000.0)
for i in range(len(a)):
    if a[i][0] * k + a[i][1] < ans and a[i][1] < k:
        ans = a[i][0] * k + a[i][1]
    if a[i][1] * k + a[i][0] < ans and a[i][0] < k:
        ans = a[i][1] * k + a[i][0]
print(ans)
