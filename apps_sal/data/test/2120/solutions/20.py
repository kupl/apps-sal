n, m = map(int, input().split())
v = list(map(int, input().split()))
r = [set() for i in range(n)]
for i in range(m):
    n1, n2 = (int(x) - 1 for x in input().split())
    r[n1].add(n2)
    r[n2].add(n1)
val = 0
for x in reversed(sorted((x, i) for i, x in enumerate(v))):
    for y in r[x[1]]:
        val += v[y]
        r[y].remove(x[1])
print(val)
