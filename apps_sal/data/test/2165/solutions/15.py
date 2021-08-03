n, T = map(int, input().split())
v = list(map(int, input().split()))
t = list(map(int, input().split()))
plus, minus = [], []
pr, ans = 0, 0
for i in range(n):
    if t[i] < T:
        minus.append([T - t[i], i])
    elif t[i] > T:
        plus.append([t[i] - T, i])
    else:
        ans += v[i]
max1, max2 = 0, 0
for i in range(len(minus)):
    max1 += minus[i][0] * v[minus[i][1]]
for i in range(len(plus)):
    max2 += plus[i][0] * v[plus[i][1]]
if max1 > max2:
    minus.sort()
    i = 0
    while pr != max2:
        if max2 - pr < v[minus[i][1]] * minus[i][0]:
            ans += (max2 - pr) / minus[i][0]
            pr += max2 - pr
        else:
            ans += v[minus[i][1]]
            pr += v[minus[i][1]] * minus[i][0]
        i += 1
    for i in range(len(plus)):
        ans += v[plus[i][1]]
else:
    plus.sort()
    i = 0
    while pr != max1:
        if max1 - pr < v[plus[i][1]] * plus[i][0]:
            ans += (max1 - pr) / plus[i][0]
            pr += max1 - pr
        else:
            ans += v[plus[i][1]]
            pr += v[plus[i][1]] * plus[i][0]
        i += 1
    for i in range(len(minus)):
        ans += v[minus[i][1]]
print(ans)
