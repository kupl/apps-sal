n, m = map(int, input().split())

l = []

for i in range(m):
    a, b = map(int, input().split())
    l.append(a)
    l.append(b)

for i in range(n):
    print(l.count(i + 1))
