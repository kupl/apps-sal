n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())
gr = [[l[i], r[i]] for i in range(n)]
m1, m2 = max(l[0], l[1]), min(l[0], l[1])
for i in range(2, n):
    if l[i] > m1:
        m1, m2, = l[i], m1
    elif l[i] > m2:
        m2 = l[i]
for i in range(n):
    if gr[i][0] == m1:
        gr[i][0] = m2
    else:
        gr[i][0] = m1
m1, m2 = min(r[0], r[1]), max(r[0], r[1])
for i in range(2, n):
    if r[i] < m1:
        m1, m2, = r[i], m1
    elif r[i] < m2:
        m2 = r[i]
for i in range(n):
    if gr[i][1] == m1:
        gr[i][1] = m2
    else:
        gr[i][1] = m1
mx = 0
for i in range(n):
    mx = max(mx, gr[i][1] - gr[i][0])
print(mx)
