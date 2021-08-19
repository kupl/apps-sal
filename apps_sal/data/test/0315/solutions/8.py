(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if a[i] - (k - a[i - 1]) < 0:
        ans += a[i] - (k - a[i - 1])
        a[i] = k - a[i - 1]
print(abs(ans))
print(*a)
