(x, y, x0, y0) = map(int, input().split())
s = input()
z = set()
k = (len(s) + 1) * [0]
k[0] = 1
u = 0
z.add((x0, y0))
for i in s:
    u += 1
    if i == 'U' and x0 > 1:
        x0 -= 1
    elif i == 'D' and x0 < x:
        x0 += 1
    elif i == 'L' and y0 > 1:
        y0 -= 1
    elif i == 'R' and y0 < y:
        y0 += 1
    if not (x0, y0) in z:
        k[u] += 1
        z.add((x0, y0))
k[len(s)] += x * y - sum(k)
for i in k:
    print(i, end=' ')
