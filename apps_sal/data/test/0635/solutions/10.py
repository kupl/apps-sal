import sys

n, s = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[0] == 0:
    print('NO')
    return

if a[s - 1]:
    print('YES')
    return

if b[s - 1]:
    for i in range(s, n):
        if a[i] and b[i]:
            print('YES')
            return

print('NO')

