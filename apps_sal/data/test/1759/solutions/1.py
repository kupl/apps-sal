m,n = map(int,input().split())
shed = []
for i in range(m):
    shed.append(list(map(int,input().split())))
time = [0] * 51
ans = []
for i in range(m):
    tt = 0
    for j in range(n):
        tt = max(tt, time[j])+ shed[i][j]
        time[j] = tt
    ans.append(tt)
print(*ans)
