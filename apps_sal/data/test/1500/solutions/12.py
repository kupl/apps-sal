n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
r = 0
i = 1
while i < n:
    if a[i] - a[i - 1] > k:
        print(-1)
        return
    elif a[i] - a[i - 1] > r:
        r = k
        ans += 1
    r -= a[i] - a[i - 1]
    i += 1
print(ans)
