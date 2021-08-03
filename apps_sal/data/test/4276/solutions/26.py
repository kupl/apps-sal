N, T = map(int, input().split())
ans = 1001
ls = []
for i in range(N):
    ls.append(list(map(int, input().split())))
for i in ls:
    if i[1] <= T:
        ans = min(ans, i[0])
    else:
        continue
if ans == 1001:
    print('TLE')
else:
    print(ans)
