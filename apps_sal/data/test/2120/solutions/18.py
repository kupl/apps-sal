(n, m) = map(int, input().split())
r = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
p = [[] for i in range(n)]
for i in range(m):
    (x, y) = map(lambda n: int(n) - 1, input().split())
    p[x] += [y]
    p[y] += [x]
q = [len(i) for i in p]
s = 0
for (x, f) in r:
    s += q[x] * f
    for y in p[x]:
        q[y] -= 1
print(s)
