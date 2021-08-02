n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = []
for i in range(n):
    cur = 0
    for j in range(n):
        if j > i:
            if a[j] == a[i] + (j - i) * k:
                cur += 1
        elif j < i:
            if a[j] == a[i] - (i - j) * k:
                cur += 1
    b.append(cur)

t, cur = -1, -1
for i in range(len(b)):
    if (b[i] > cur) and (a[i] > k * i):
        cur = b[i]
        t = i

res = []
for i in range(n):
    c = - a[i] + ((i - t) * k + a[t])
    if c != 0:
        res.append([i + 1, c])

print(len(res))
for i, j in res:
    if j < 0:
        print('-', str(i), -j)
    else:
        print('+', str(i), j)
