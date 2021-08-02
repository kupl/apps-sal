n, m = map(int, input().split())
lis = [list(map(int, input().split())) for i in range(n)]
lis.sort()
cnt = 0
mon = 0
i = 0
if n >= 2:
    while cnt < m:
        if lis[i][1] + cnt < m:
            cnt += lis[i][1]
            mon += lis[i][0] * lis[i][1]
            i += 1
        else:
            break
    print(mon + (m - cnt) * lis[i][0])
else:
    print(m * lis[0][0])
