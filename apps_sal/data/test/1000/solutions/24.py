n, v = map(int, input().split())
m = min(n - 1, v)
ans = m
for i in range(2, n + 1 - m):
    ans += i
print(ans)
