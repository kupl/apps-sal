(n, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = []
for i in range(n):
    c.append([b[i] - a[i], a[i], b[i]])
c = sorted(c, key=lambda x: -x[0])
m = 0
for i in range(n):
    if i < k or c[i][1] <= c[i][2]:
        m += c[i][1]
    else:
        m += c[i][2]
print(m)
