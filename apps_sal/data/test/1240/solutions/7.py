n = int(input())
l = []
r = []
for i in range(n):
    li, ri = list(map(int, input().split(' ')))
    l.append(li)
    r.append(ri)
L = sum(l)
R = sum(r)
beauty = abs(L - R)
best = -1
for i in range(n):
    LL = L - l[i] + r[i]
    RR = R - r[i] + l[i]
    pos_beauty = abs(LL - RR)
    if pos_beauty > beauty:
        beauty = pos_beauty
        best = i
print(best + 1)
