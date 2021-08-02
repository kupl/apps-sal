n = int(input())
a = []
for i in range(n):
    a.append([input(), 0])
m = int(input())
b = []
for i in range(m):
    b.append([input(), 0])

res = 0
for i in range(n):
    c = 0
    if a[i][1] == 0:
        a[i][1] = 1
        for j in range(i, n):
            if a[i][0] == a[j][0]:
                c += 1
                a[j][1] = 1
        for j in range(m):
            if a[i][0] == b[j][0]:
                c -= 1
    res = max(res, c)
print(res)
