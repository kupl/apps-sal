n, m, q = [int(i) for i in input().split()]
t = []
u = []
for i in range(n):
    t.append([int(i) for i in input().split()])
    s = 0
    o = 0
    for k in t[-1]:
        if k == 1:
            s += 1
            o = max(s, o)
        else:
            s = 0
    u.append(o)
answer = []
for i in range(q):
    a, b = [int(i) - 1 for i in input().split()]
    if t[a][b] == 1:
        t[a][b] = 0
    else:
        t[a][b] = 1
    s = 0
    o = 0
    for k in t[a]:
        if k == 1:
            s += 1
            o = max(s, o)
        else:
            s = 0
    u[a] = o
    answer.append(max(u))
for i in answer:
    print(i)
