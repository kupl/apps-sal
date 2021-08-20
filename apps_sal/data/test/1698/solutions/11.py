(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
ans = 0
for i in range((n - 1) // k + 1):
    ans += a[i * k] - 1
print(ans * 2)
