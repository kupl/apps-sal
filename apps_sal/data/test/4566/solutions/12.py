(n, m) = map(int, input().split())
c = []
for _ in range(m):
    (a, b) = map(str, input().split())
    c.append(a)
    c.append(b)
for i in range(1, n + 1):
    print(c.count(str(i)))
