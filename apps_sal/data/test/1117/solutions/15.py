n = int(input())
p = []
flag = True
q = []
for i in range(n):
    (x, y) = map(int, input().split())
    p.append((x, y))
q.append(max(p[0][0], p[0][1]))
for i in range(1, n):
    if q[i - 1] >= p[i][0] and q[i - 1] < p[i][1]:
        q.append(p[i][0])
    elif q[i - 1] < p[i][0] and q[i - 1] >= p[i][1]:
        q.append(p[i][1])
    elif q[i - 1] >= p[i][0] and q[i - 1] >= p[i][1]:
        q.append(max(p[i][1], p[i][0]))
    else:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
