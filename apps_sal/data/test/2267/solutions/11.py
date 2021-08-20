from functools import cmp_to_key


def cmp(a, b):
    x = a + b
    y = b + a
    if x < y:
        return -1
    elif x == y:
        return 0
    return 1


(n, a) = (int(input()), [])
for i in range(n):
    a.append(input())
a.sort(key=cmp_to_key(cmp))
for i in a:
    print(i, end='')
