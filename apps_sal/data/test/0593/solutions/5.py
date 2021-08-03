n, m = list(map(int, input().split(' ')))
c = []
for i in range(m):
    c.append(list(map(int, input().split(' '))))
d = []
for i in range(n):
    d.append(0)
for i in c:
    d[i.index(max(i))] += 1
print(d.index(max(d)) + 1)
