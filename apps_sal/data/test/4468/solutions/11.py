(n, t) = map(int, input().split())
T = tuple(map(int, input().split()))
ans = 0
for i in range(0, n - 1):
    dt = T[i + 1] - T[i]
    ans += min(dt, t)
print(ans + t)
