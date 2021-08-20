(n, m) = map(int, input().split(' '))
a = []
for i in range(m):
    a.append(list(map(int, input().split(' '))))
v = [0] * n
for aa in a:
    v[aa.index(max(aa))] += 1
print(v.index(max(v)) + 1)
