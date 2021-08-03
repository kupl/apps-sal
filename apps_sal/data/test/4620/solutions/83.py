from math import *

n = int(input()) - 1
c = [0] * n
s = [0] * n
f = [0] * n
for i in range(n):
    c[i], s[i], f[i] = map(int, input().split())

for i in range(n):
    a = s[i] + c[i]
    for j in range(i + 1, n):
        if a <= s[j]:
            a = s[j] + c[j]
        else:
            a = s[j] + f[j] * ceil((a - s[j]) / f[j]) + c[j]
    print(a)
print(0)
