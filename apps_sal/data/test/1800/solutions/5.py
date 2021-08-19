(n, m) = map(int, input().split())
a = list(map(int, input().split()))
t = list()
b = list()
for i in range(m):
    (x, y) = map(int, input().split())
    while len(t) > 0 and y >= t[-1][1]:
        t.pop()
    t.append([x, y])
(x, y) = (0, t[0][1] - 1)
t.append([0, 0])
b = sorted(a[:y + 1])
for i in range(1, len(t)):
    for j in range(t[i - 1][1], t[i][1], -1):
        if t[i - 1][0] == 1:
            a[j - 1] = b[y]
            y -= 1
        else:
            a[j - 1] = b[x]
            x += 1
print(' '.join(list((str(i) for i in a))))
