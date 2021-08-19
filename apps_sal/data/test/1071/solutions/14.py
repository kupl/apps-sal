from math import ceil
(a, b, c) = map(int, input().split())
(d, e, f) = map(int, input().split())
n = int(input())
k = a + b + c
l = d + e + f
if ceil(k / 5) + ceil(l / 10) <= n:
    print('YES')
else:
    print('NO')
