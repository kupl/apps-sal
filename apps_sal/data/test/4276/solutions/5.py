N, T = map(int, input().split())
ans = 1001
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)

if ans <= 1000:
    print(ans)
else:
    print("TLE")
