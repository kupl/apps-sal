(N, T) = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]
cost = 9999
for i in range(N):
    if CT[i][1] <= T:
        if CT[i][0] < cost:
            cost = CT[i][0]
if cost == 9999:
    print('TLE')
else:
    print(cost)
pass
