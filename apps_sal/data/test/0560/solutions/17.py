(r, c) = list(map(int, input().split()))
l = [0] * c
h = [0] * r
a = []
for i in range(r):
    a.append([])
    ls = list(input())
    for j in range(c):
        a[i].append(ls[j])
        if a[i][j] != '.':
            l[j] = 1
            h[i] = 1
        else:
            a[i][j] = 1
t = 0
for i in range(r):
    if h[i] == 0:
        for j in range(c):
            t += a[i][j]
            a[i][j] = 0
for i in range(c):
    if l[i] == 0:
        for j in range(r):
            t += a[j][i]
            a[j][i] = 0
print(t)
