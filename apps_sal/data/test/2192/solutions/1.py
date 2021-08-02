n = int(input())
w = []; a = []; b = []
for i in range(n):
    w.append(list(map(int, input().split())))
    a.append(list(range(n)))
    b.append(list(range(n)))
for i in range(n):
    for j in range(n):
        a[i][j] = (w[i][j] + w[j][i]) / 2
        b[i][j] = (w[i][j] - w[j][i]) / 2
for i in range(n):
    for j in range(n):
        print('{0:0.8f}'.format(a[i][j]), end=' ')
    print()
for i in range(n):
    for j in range(n):
        print('{0:0.8f}'.format(b[i][j]), end=' ')
    print()
