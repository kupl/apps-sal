n = int(input())
ls = set()
pts = []
for i in range(n):
    x, y = list(map(int, input().split()))
    pts.append([x, y])
for i in range(n):
    for j in range(i + 1, n):
        x1 = pts[i][0]
        y1 = pts[i][1]
        x2 = pts[j][0]
        y2 = pts[j][1]
        m = (y2 - y1) / (x2 - x1) if x2 != x1 else 'I'
        c = (x2 * y1 - x1 * y2) / (x2 - x1) if x1 != x2 else x1
        ls.add((m, c))
ins = set()
ls = list(ls)
nls = len(ls)
for i in range(nls):
    for j in range(i + 1, nls):
        m1 = ls[i][0]
        m2 = ls[j][0]
        if m1 != m2:
            x = [i, j]
            x.sort()
            ins.add(tuple(x))
print(len(ins))


