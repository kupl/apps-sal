n = int(input())
ans = 0
for i in range(n):
    ans += (i + 1) * (n - i)
for i in range(n-1):
    u, v = map(int, input().split())
    ans -= min(u, v) * (n - max(u, v) + 1)
print(ans)
