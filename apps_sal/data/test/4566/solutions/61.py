n, m = map(int, input().split())

l = []
for i in range(m):
    x, y = map(int, input().split())
    l.append(x)
    l.append(y)

for i in range(n):
    print(l.count(i + 1))
