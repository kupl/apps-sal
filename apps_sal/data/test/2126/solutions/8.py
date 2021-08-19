def kk():
    return list(map(int, input().split()))


def ll():
    return list(kk())


(n, m, h) = kk()
front = ll()
left = ll()
for col in range(n):
    tbp = []
    line = kk()
    for (row, l) in enumerate(line):
        tbp.append(0 if l == 0 else min(front[row], left[col]))
    print(*tbp)
