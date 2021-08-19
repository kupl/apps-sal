(n, m) = list(map(int, input().split()))
a = [int(el) for el in input().split()]
b = [0] * 101
for i in range(m):
    b[a[i]] += 1
d = []
for i in b:
    if i != 0:
        d.append([i, 0])


def f(df):
    return -df[0]


d.sort(key=f)
k = 0
l = 0
for i in range(n):
    nm = 0
    mm = d[0][0] // (d[0][1] + 1)
    for j in range(len(d)):
        if mm < d[j][0] // (d[j][1] + 1):
            nm = j
            mm = d[j][0] // (d[j][1] + 1)
    d[nm][1] += 1
print(mm)
