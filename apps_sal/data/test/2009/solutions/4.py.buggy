n = int(input())
r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
g = []
for i in range(n):
    g.append(input())

d1 = {(r1, c1)}
q = [(r1, c1)]
while q:
    v = q[0]
    r, c = v
    if r == r2 and c == c2:
        print(0)
        return
    q = q[1:]
    if r + 1 >= 0 and r + 1 < n:
        nv = (r + 1, c)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d1:
                d1.add(nv)
                q.append(nv)
    if r - 1 >= 0 and r - 1 < n:
        nv = (r - 1, c)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d1:
                d1.add(nv)
                q.append(nv)
    if c + 1 >= 0 and c + 1 < n:
        nv = (r, c + 1)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d1:
                d1.add(nv)
                q.append(nv)
    if c - 1 >= 0 and c - 1 < n:
        nv = (r, c - 1)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d1:
                d1.add(nv)
                q.append(nv)

d2 = {(r2, c2)}
q = [(r2, c2)]
while q:
    v = q[0]
    r, c = v
    q = q[1:]
    if r + 1 >= 0 and r + 1 < n:
        nv = (r + 1, c)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d2:
                d2.add(nv)
                q.append(nv)
    if r - 1 >= 0 and r - 1 < n:
        nv = (r - 1, c)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d2:
                d2.add(nv)
                q.append(nv)
    if c + 1 >= 0 and c + 1 < n:
        nv = (r, c + 1)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d2:
                d2.add(nv)
                q.append(nv)
    if c - 1 >= 0 and c - 1 < n:
        nv = (r, c - 1)
        if g[nv[0]][nv[1]] == '0':
            if nv not in d2:
                d2.add(nv)
                q.append(nv)
ans = 10**18
for v1 in d1:
    for v2 in d2:
        ans = min(ans, (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
print(ans)
