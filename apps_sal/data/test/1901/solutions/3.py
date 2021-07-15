def bfs(i):
    nonlocal p, f, v

    q = [i]
    qi = 0
    
    v[i] = 1
  
    best = p[i]

    while qi < len(q):
        j = q[qi]
        if p[j] < best:
            best = p[j]
        for k in f[j]:
            if v[k] != 1:
                q.append(k)
                v[k] = 1
        qi += 1

    return best

n, m = [int(i) for i in input().split(" ")]

p = [int(i) for i in input().split(" ")]
v = [0]*n
f = {}

for a in range(n):
    f[a] = []

for a in range(m):
    x, y = [int(i) for i in input().split(" ")]
    f[x-1].append(y-1)
    f[y-1].append(x-1)

cost = 0
for i in range(n):
    if v[i] == 0:
        cost += bfs(i)

print(cost)



