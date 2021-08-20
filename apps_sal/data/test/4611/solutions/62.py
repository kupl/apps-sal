N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
pret = prex = prey = 0
f = 1
for i in range(N):
    t = P[i][0]
    x = P[i][1]
    y = P[i][2]
    td = t - pret
    xd = abs(x - prex)
    yd = abs(y - prey)
    diff = xd + yd
    if td < diff:
        f = 0
        break
    if (td - diff) % 2 == 0:
        pret = t
        prex = x
        prey = y
        continue
    else:
        f = 0
        break
if f == 1:
    print('Yes')
else:
    print('No')
