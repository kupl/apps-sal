(n, t) = map(int, input().split())
ct = [list(map(int, input().split())) for i in range(n)]
flag = 0
ans = ct[0][0]
for i in range(n):
    if ct[i][1] <= t:
        flag = 1
        ans = min(ans, ct[i][0])
    else:
        pass
if flag == 0:
    print('TLE')
else:
    print(ans)
