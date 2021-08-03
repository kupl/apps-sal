n = int(input())
p = []
q = []
c = 1
for i in range(n):
    a, b = list(map(str, input().split()))
    if a not in q:
        p.append([a, b])
        q.append(a)
        q.append(b)
    else:
        x = q.index(p[int(q.index(a) / 2 - .5)][1])
        p[int(q.index(a) / 2 - .5)][1] = b
        q[x] = b

print(len(p))
for i in range(len(p)):
    print(p[i][0], p[i][1])
