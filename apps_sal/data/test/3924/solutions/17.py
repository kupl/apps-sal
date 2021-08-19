(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(0, len(a) - 1):
    ans += a[i] // k
    ans += int(a[i] % k != 0)
    a[i + 1] += a[i] % k
    a[i + 1] = max(a[i + 1] - int(a[i] % k != 0) * k, 0)
ans += a[len(a) - 1] // k + int(a[-1] % k != 0)
print(ans)
