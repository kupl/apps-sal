n, s = map(int, input().split())
a = [0] * (s + 1)
for i in range(n):
    x, y = map(int, input().split())
    a[x] = max(a[x], y)
ans = -1
for i in range(s, 0, -1):
    ans = max(ans + 1, a[i])
print(ans + 1)
