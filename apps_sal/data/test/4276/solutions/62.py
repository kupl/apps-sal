N, T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]

ans = 1001
for ct in CT:
    if ct[1] <= T:
        ans = min(ans, ct[0])

if ans == 1001:
    print('TLE')
else:
    print(ans)
