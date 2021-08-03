def read(): return list(map(int, input().split()))


n, m = read()
a = list(read())
t = []
for i in range(m):
    x, r = read()
    while len(t) and r >= t[-1][1]:
        t.pop()
    t.append((x, r))
x, r = 0, t[0][1] - 1
t.append((0, 0))
b = sorted(a[:r + 1])
for i in range(1, len(t)):
    for j in range(t[i - 1][1], t[i][1], -1):
        if t[i - 1][0] == 1:
            a[j - 1] = b[r]
            r -= 1
        else:
            a[j - 1] = b[x]
            x += 1
print(*a)
