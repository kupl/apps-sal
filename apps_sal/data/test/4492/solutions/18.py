N, x = map(int, input().split())
a = list(map(int, input().split()))

y = min(a[0], x)
ans = a[0]-y
for i in range(1, N):
    z = a[i]
    w = max(y+z-x, 0)
    y = z-w
    ans += w

print(ans)
