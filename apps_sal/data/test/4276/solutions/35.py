N, T = map(int, input().split())

ans = "TLE"
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if ans == "TLE" or ans > c:
            ans = c

print(ans)
