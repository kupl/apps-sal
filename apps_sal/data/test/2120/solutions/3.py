(n, m) = map(int, input().split())
f = [int(x) for x in input().split()]
ans = 0
for i in range(m):
    (a, b) = map(int, input().split())
    ans += min(f[a - 1], f[b - 1])
print(ans)
