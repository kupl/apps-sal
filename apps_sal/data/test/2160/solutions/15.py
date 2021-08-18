import sys

n, k = list(map(int, input().split()))
lis = list(map(int, input().split()))

v = [0] * (n + 2)
p = [0] * (n + 2)
c = [0] * n
for i in lis:
    i -= 1
    c[i] = 1
    if i + 1 < n and c[i + 1] == 1:
        v[i + 1] = 1
    if i - 1 >= 0 and c[i - 1] == 1:
        p[i - 1] = 1

x = 0
for i in lis:
    i -= 1
    if c[i]:
        x += c[i] + v[i] + p[i]
    else:
        if i + 1 < n:
            x += c[i + 1]
        if i - 1 >= 0:
            x += c[i - 1]
x = 0
for i in range(0, n):
    x += c[i] + v[i + 1] + p[i - 1]
print(3 * n - 2 - x)
