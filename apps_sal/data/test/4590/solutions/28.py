n, m, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = [0]
for i in range(n):
    if c[i] + a[i] <= k:
        c.append(c[i] + a[i])
    else:
        break

d = [0]
for i in range(m):
    if d[i] + b[i] <= k:
        d.append(d[i] + b[i])
    else:
        break

e = 0
f = len(d) - 1
for i in range(len(c)):
    for j in range(f, -1, -1):
        if c[i] + d[j] <= k:
            if i + j > e:
                e = i + j
            f = j
            break
print(e)
