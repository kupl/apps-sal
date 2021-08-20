import sys
(n, m) = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
c1 = []
c2 = []
for i in range(n):
    c1.append(a[i].count(1))
for i in range(m):
    c = 0
    for j in range(n):
        if a[j][i] == 1:
            c += 1
    c2.append(c)
s = 0
for i in c1:
    s += 2 ** i - 2 + 2 ** (m - i)
for i in c2:
    s += 2 ** i - 2 + 2 ** (n - i)
s -= n * m
print(s)
