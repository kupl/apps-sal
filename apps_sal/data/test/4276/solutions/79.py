N, T = map(int, input().split())

ans = 2000
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(c, ans)

print(ans if ans != 2000 else "TLE")
