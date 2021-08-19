# coding:utf-8
n, m = map(int, input().split())
L = 1
R = n
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = (b, a)
    L = max(a, L)
    R = min(b, R)
if R - L <= 0:
    print(0)
else:
    print(R - L)
