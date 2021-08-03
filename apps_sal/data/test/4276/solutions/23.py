n, t = map(int, input().split())
ans = 1001
for i in range(n):
    c, time = map(int, input().split())
    if time <= t:
        ans = min(ans, c)
if ans == 1001:
    print("TLE")
else:
    print(ans)
