n = int(input())
c = input()
c = c.split()
c = list(map(int, c))
r = []
for i in range(200):
    t = 0
    for j in range(n):
        if (c[j] > 0):
            c[j] -= 1
            t += 1
    r.append(t)
c2 = []
for i in range(n):
    t = 0
    for j in range(200):
        if (r[j] > 0):
            r[j] -= 1
            t += 1
    c2.append(t)
c2.reverse()
for i in c2:
    print(i, end=' ')
