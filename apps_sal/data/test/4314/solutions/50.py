(h, w) = map(int, input().split())
a = [list(input()) for _ in range(h)]
x = list()
y = list()
for i in range(h):
    if '#' in a[i]:
        x.append(i)
for j in range(w):
    cnt = 0
    for k in range(h):
        if a[k][j] == '#':
            y.append(j)
            break
for p in x:
    z = ''
    for q in y:
        z += a[p][q]
    print(z)
