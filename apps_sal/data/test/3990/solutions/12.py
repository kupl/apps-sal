(n, m) = list(map(int, input().split()))
a = [[] for i in range(n)]
r = False
for i in range(m):
    (x, y) = list(map(int, input().split()))
    if (x, y) == (1, n) or (x, y) == (n, 1):
        r = True
    a[x - 1].append(y - 1)
    a[y - 1].append(x - 1)
if r:
    for i in range(n):
        s = set(a[i])
        a[i] = [j for j in range(n) if i != j and (not j in s)]
q = [(0, 0)]
v = set([0])
l = 0
while l < len(q):
    (x, d) = q[l]
    l += 1
    for y in a[x]:
        if not y in v:
            if y == n - 1:
                print(d + 1)
                quit()
            q.append((y, d + 1))
            v.add(y)
print(-1)
