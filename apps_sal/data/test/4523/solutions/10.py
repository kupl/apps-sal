import math

T = int(input())

for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    d = False

    a.sort()

    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print('NO')
            d = True
            break

    if not d:
        print('YES')
