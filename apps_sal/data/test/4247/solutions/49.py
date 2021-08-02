n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(1, n - 1):
    pl = [p[i - 1], p[i], p[i + 1]]
    if p[i] != max(pl) and p[i] != min(pl):
        ans += 1
print(ans)
