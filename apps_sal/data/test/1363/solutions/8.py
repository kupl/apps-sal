_ = input()
a = list([(int(x), 1) for x in input().split()])
a.extend([(int(x), 2) for x in input().split()])
a.extend([(int(x), 3) for x in input().split()])
a.sort()
g, d, f, n = [0], [0], [0], len(a)
for x, y in a:
    g.append(g[-1])
    d.append(d[-1])
    f.append(f[-1])
    if y == 1:
        g[-1] += 1
    elif y == 2:
        d[-1] += 1
    else:
        f[-1] += 1

s = i = 0
j = 1

while i < n:
    while j < n and a[j][0] <= 2 * a[i][0]:
        j += 1
    j -= 1
    g1 = g[j + 1] - g[i]
    d1 = d[j + 1] - d[i]
    f1 = f[j + 1] - f[i]
    # print(i, j, g1, d1, f1)
    if a[i][1] == 1:
        s += d1 * (d1 - 1) * f1 * (f1 - 1) * (f1 - 2) // 12
    elif a[i][1] == 2:
        s += g1 * (d1 - 1) * f1 * (f1 - 1) * (f1 - 2) // 6
    else:
        s += g1 * d1 * (d1 - 1) * (f1 - 1) * (f1 - 2) // 4
    i += 1

print(s)
