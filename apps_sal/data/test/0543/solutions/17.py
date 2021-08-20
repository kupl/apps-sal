import sys
n = int(input())
a = [int(i) for i in input().split(' ')]
k = 0
if n == 1:
    if a[0] % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    k = 0
    for i in range(n - 1):
        if a[i] < 0:
            k = 1
        elif a[i] % 2 == 1:
            a[i + 1] -= 1
    if a[n - 1] % 2 == 1:
        k = 1
    if k == 1:
        print('NO')
    else:
        print('YES')
