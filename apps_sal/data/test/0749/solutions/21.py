a = input()
d = 'abcdefghijklmnopqrstuvwxyz'
m = [[-1] for i in range(26)]
n = 0
for i in range(len(a)):
    k = d.index(a[i])
    if len(m[k]) == 1:
        m[k] += [i]
        m[k] += [m[k][1] - m[k][0]]
    else:
        m[k][0] = m[k][1]
        m[k][1] = i
        if m[k][2] < m[k][1] - m[k][0]:
            m[k][2] = m[k][1] - m[k][0]
for i in range(26):
    if len(m[i]) == 3:
        m[i][0] = m[i][1]
        m[i][1] = len(a)
        if m[i][2] < m[i][1] - m[i][0]:
            m[i][2] = m[i][1] - m[i][0]
g = []
j = 0
for i in range(26):
    if len(m[i]) == 3:
        k = a[0:m[i][2]]
        n = a[len(a) - m[i][2]:]
        if k.count(d[i]) > 0 and n.count(d[i]) > 0:
            g += [m[i][2]]
j = len(a) // 2 + 1
if len(g) != 0 and j > min(g):
    print(min(g))
else:
    print(j)
