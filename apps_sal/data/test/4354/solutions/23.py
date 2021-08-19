(n, m) = list(map(int, input().split()))
lx = []
ly = []
for i in range(n + m):
    (x, y) = list(map(int, input().split()))
    lx.append(x)
    ly.append(y)
for i in range(n):
    r = []
    for j in range(n, m + n):
        r.append(abs(lx[i] - lx[j]) + abs(ly[i] - ly[j]))
    print(r.index(min(r)) + 1)
