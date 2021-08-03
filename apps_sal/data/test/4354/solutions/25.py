n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
c = []
for i in range(m):
    c.append([int(x) for x in input().split()])

for i in range(n):
    d = 10 ** 9
    cc = 0
    for j in range(m):
        di = abs(a[i][0] - c[j][0]) + abs(a[i][1] - c[j][1])
        if di < d:
            d = di
            cc = j
    print(cc + 1)
