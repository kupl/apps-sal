n,m,x = list(map(int,input().split()))
ca = [list(map(int,input().split())) for _ in range(n)]

c = []
a = []
for i in range(n):
    c.append(ca[i][0])
    a.append(ca[i][1:])

INF = 10**9
ans = INF
for i in range(1<<n):
    skill = [0]*m
    sum_cost = 0
    for j in range(n):
        if (i >> j)&1:
            for k in range(m):
                skill[k] += a[j][k]
            sum_cost += c[j]
    if min(skill) >= x:
        ans = min(ans,sum_cost)

if ans == INF:
    print((-1))
else:
    print(ans)

