a = []
for i in range(3):
    a.append(list(map(int, input().split())))

p = sum(a[2]) - sum(a[0])
q = a[0][2] + a[2][0]
a[0][0] = (p + q) // 2;
a[2][2] = q - a[0][0]
a[1][1] = sum(a[0]) - sum(a[1])

for i in range(3):
    print("%d %d %d" % (a[i][0], a[i][1], a[i][2]))


