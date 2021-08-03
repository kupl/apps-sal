n = int(input())
UV = [list(map(int, input().split())) for _ in range(n - 1)]

ans = 0
for i in range(1, n + 1):
    ans += i * (i + 1) // 2

for uv in UV:
    u, v = sorted(uv)
    ans -= u * (n - v + 1)

print(ans)
