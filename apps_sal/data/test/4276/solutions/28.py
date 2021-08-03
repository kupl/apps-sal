N, T = list(map(int, input().split()))
ans = 100000
for _ in range(N):
    c, t = list(map(int, input().split()))
    if t <= T:
        ans = min(ans, c)
print(('TLE' if ans == 100000 else ans))
