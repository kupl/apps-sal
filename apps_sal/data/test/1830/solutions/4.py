n, m = map(int, input().split())

c = set()
r = set()

for i in range(m):
    x, y = map(int, input().split())
    c.add(x)
    r.add(y)

    c1 = len(c)
    r1 = len(r)
    #print(c1, r1)

    print((n * n) - (c1 * n + ((n - c1) * r1)), end=" ")

print("")
