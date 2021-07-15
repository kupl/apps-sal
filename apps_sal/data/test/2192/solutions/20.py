x = int(input())

l = list()
for i in range(x):
    l.append([int(a) for a in input().split()])

a, b = list(range(x)), list(range(x))
for i in range(x):
    a[i], b[i] = list(range(x)), list(range(x))
    for j in range(x):
        if i is j:
            a[i][j] = l[i][j]
            b[i][j] = 0
        else:
            a[i][j] = (l[i][j] + l[j][i]) / 2
            b[i][j] = l[i][j] - a[i][j]

for x in a:
    print(" ".join(["{:.8f}".format(float(i)) for i in x]))

for x in b:
    print(" ".join(["{:.8f}".format(float(i)) for i in x]))

