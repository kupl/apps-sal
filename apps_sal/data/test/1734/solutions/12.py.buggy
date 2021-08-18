n = int(input())
num = []
for i in range(n):
    num.append(input())
d = {}
q = []
for i in range(n):
    r = {}
    g = []
    for j in range(0, 9):
        for l in range(j + 1, 10):
            t = num[i][j:l]
            g.append(t)
            if t in r:
                continue
            r[t] = 1
            if t in d:
                d[t] = d[t] + 1
            else:
                d[t] = 1
    g.sort(key=len)
    q.append(g)
if n == 1:
    print(num[0][0])
    return
answ = []
for i in range(n):
    for j in q[i]:
        if d[j] == 1:
            answ.append(j)
            break
for i in answ:
    print(i)
