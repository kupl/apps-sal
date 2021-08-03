N, T = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(N)]

ans = 1001
for p in ct:
    if p[1] <= T:
        ans = min(ans, p[0])

print(ans if ans != 1001 else "TLE")
