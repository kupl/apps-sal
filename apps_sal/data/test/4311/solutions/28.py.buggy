import sys
import copy
s = int(input())


def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


for i in range(1000000):
    if i == 0:
        a = [s]
    else:
        a.append(f(a[i - 1]))

    if a.count(a[i]) == 2:
        print((i + 1))
        return
