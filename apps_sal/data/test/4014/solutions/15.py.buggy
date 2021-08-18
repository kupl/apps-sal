def R(): return list(map(int, input().split()))


n, m = R()
a = []
for i in range(m):
    s, d, c = R()
    a.append([d, s, c, i + 1])
a.sort()
r = [0] * (n + 1)
for i in range(m):
    r[a[i][0]] = m + 1
for i in range(m):
    for j in range(a[i][1], a[i][0]):
        if a[i][2] == 0:
            break
        elif r[j] == 0:
            r[j] = a[i][3]
            a[i][2] -= 1
    if a[i][2]:
        print((-1))
        return
print(*r[1:])
