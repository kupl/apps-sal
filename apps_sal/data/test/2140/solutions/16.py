import sys
x = input()
l = len(x)
a = int(input())
b = map(int, sys.stdin.readline().split())
rv = [False] * (l // 2 + 1)
for i in b:
    rv[i] = not rv[i]
sumx = [0] * len(x) + [0]
pt = 0
for i in range(1, l // 2 + 1):
    sumx[i] = sumx[i - 1] + rv[i]
for i in range(l // 2):
    if sumx[i + 1] % 2 == 1:
        print(x[l - 1 - i], end='')
    else:
        print(x[i], end='')
if l % 2 == 1:
    print(x[l // 2], end='')
for i in range(l // 2, l):
    if i == l // 2 and l % 2 == 1:
        continue
    if sumx[l - i] % 2 != 1:
        print(x[i], end='')
    else:
        print(x[l - 1 - i], end='')
