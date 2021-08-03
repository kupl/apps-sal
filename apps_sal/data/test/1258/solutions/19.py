n = int(input())
q = []
qh = {}
qc = {}
for i in range(n):
    qh[i] = []
    qc[i] = 0
for i in range(n - 2):
    q1, q2, q3 = list(map(int, input().split()))
    q.append([q1 - 1, q2 - 1, q3 - 1])
    for d in [q1, q2, q3]:
        qh[d - 1].append(i)
        qc[d - 1] += 1
pp = []
for i in range(n):
    if qc[i] == 1:
        pp.append(i)
p1, p2 = pp
p3 = -1
p4 = -1
for i in q[qh[p2][0]]:
    if qc[i] == 3:
        p3 = i
    if qc[i] == 2:
        p4 = i
p5, p6 = -1, -1
for i in q[qh[p1][0]]:
    if qc[i] == 3:
        p5 = i
    if qc[i] == 2:
        p6 = i
    qc[i] -= 1
p = [p1, p6, p5]
d = qh[p6][0]
if d == qh[p1][0]:
    d = qh[p6][1]
for i in q[d]:
    qc[i] -= 1
for i in range(n - 6):
    fg = p[-1]
    d = -1
    for j in qh[fg]:
        if j not in qh[p[-2]]:
            d = j
    for j in q[d]:
        if qc[j] == 2:
            p.append(j)
        qc[j] -= 1
if n != 5:
    p.append(p3)
p.append(p4)
p.append(p2)
print(' '.join([str(x + 1) for x in p]))
