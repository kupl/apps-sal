(n, m) = list(map(int, input().split(' ')))
d = []
for i in range(m):
    d.append(list(map(int, input().split(' '))))
ispossible = True
maxheights = []
maxheights.append(d[0][1] + d[0][0] - 1)
maxheights.append(d[-1][1] + n - d[-1][0])
for i in range(m - 1):
    d1 = d[i]
    d2 = d[i + 1]
    if abs(d2[1] - d1[1]) > d2[0] - d1[0]:
        ispossible = False
    maxheights.append((d1[1] + d2[1] + d2[0] - d1[0]) // 2)
if ispossible:
    print(max(maxheights))
else:
    print('IMPOSSIBLE')
