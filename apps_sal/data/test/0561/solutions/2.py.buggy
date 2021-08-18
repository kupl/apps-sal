# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(-1)
    return

a.sort()

d = a[1] - a[0]
if n == 2:
    if d == 0:
        print(1)
        print(a[0])
    elif d % 2 == 1:
        print(2)
        print(a[0] - d, a[1] + d)
    else:
        print(3)
        print(a[0] - d, sum(a) // 2, a[1] + d)
    return

d_list = [a[i] - a[i - 1] for i in range(1, n)]

# 对d_list分类讨论：
# 1. 所有值相同
# 2. 只有一个值与其他值不同，且为其他值的2倍
# 3. 其他情况

d2c = {}
for d in d_list:
    if d not in d2c:
        d2c[d] = 1
    else:
        d2c[d] += 1

if len(d2c) == 1:
    (d1, c1) = d2c.popitem()
    if d1 == 0:
        print(1)
        print(a[0])
    else:
        print(2)
        print(a[0] - d, a[-1] + d)
    return

if len(d2c) == 2:
    (d1, c1) = d2c.popitem()
    (d2, c2) = d2c.popitem()
    if c1 == 1 and d1 == d2 * 2:
        print(1)
        print(a[d_list.index(d1)] + d2)
    elif c2 == 1 and d2 == d1 * 2:
        print(1)
        print(a[d_list.index(d2)] + d1)
    else:
        print(0)
else:
    print(0)
