n, m = map(int, input().split())
l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

l.sort()
c = 0
for a, b in l:
    c += min(b, m) * a
    m = max(m - b, 0)

print(c)
