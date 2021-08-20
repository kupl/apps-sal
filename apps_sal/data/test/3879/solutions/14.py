__author__ = 'pxy'
n = int(input())
c = [int(i) for i in input().split()]
for j in range(n):
    while c[j] % 2 == 0:
        c[j] = c[j] // 2
    while c[j] % 3 == 0:
        c[j] = c[j] // 3
f = True
for j in range(n - 1):
    if c[j] != c[j + 1]:
        f = False
        break
if f:
    print('Yes')
else:
    print('No')
