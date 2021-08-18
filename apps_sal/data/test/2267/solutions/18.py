from functools import cmp_to_key
n = int(input())
a = []
for i in range(n):
    a.append(input())


def cmp(x, y):
    if x + y < y + x:
        return -1
    elif x + y > y + x:
        return 1
    else:
        return 0


print(''.join(sorted(a, key=cmp_to_key(cmp))))
