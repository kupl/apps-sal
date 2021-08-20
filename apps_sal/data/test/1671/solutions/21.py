from math import *
n = int(input())
a = list(map(int, input().split(' ')))
b = []
x = 0
y = 0
sm = 0
k = 0
o = 0
for i in range(n):
    sm += a[i]
k = sm // n
for i in range(n):
    b.append(k)
    if i < sm % n:
        b[i] += 1
a.sort()
b.sort()
for i in range(n):
    o += abs(a[i] - b[i])
print(o // 2)
