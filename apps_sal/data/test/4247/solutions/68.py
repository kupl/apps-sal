n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    M = max(p[i - 1], p[i], p[i + 1])
    m = min(p[i - 1], p[i], p[i + 1])
    if p[i] != M and p[i] != m: ans += 1

print(ans)
