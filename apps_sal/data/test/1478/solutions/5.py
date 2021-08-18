a = input().split(',')
o = 0
for i in range(1, len(a), 2):
    a[i] = int(a[i])
b = [[] for i in range(300000)]
c = []
for i in range(0, len(a), 2):
    b[len(c)] += [a[i]]
    if a[i + 1] == 0:
        if len(c) != 0:
            c[len(c) - 1] -= 1
    else:
        if len(c) != 0:
            c[len(c) - 1] -= 1
        c += [a[i + 1]]
    while len(c) > 0 and c[len(c) - 1] == 0:
        c.pop()
    o = max(o, len(c))
print(o + 1)
for i in range(300000):
    if b[i] == []:
        break
    else:
        print(*b[i])
