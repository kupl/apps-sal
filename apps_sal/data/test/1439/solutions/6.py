n, m = [int(i) for i in input().split()]
r = [False] * m
for x in [int(i)%m for i in input().split()]:
    c = r.copy()
    c[x] = True
    for i in range(m):
        if r[i]:
            c[(i+x)%m] = True
    r = c.copy()
    if r[0]:
        print("YES")
        return
print("NO")
