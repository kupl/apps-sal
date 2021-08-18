import time


def snake(a, b):
    if a == 0 or a == 2:
        return '
    elif a == 1:
        return '.' * (n - 1) + '
    return '


m, n = list(map(int, input().split()))
p = 0
s = ''
for i in range(m):
    s += snake(p, n) + '\n'
    p = (p + 1) % 4

print(s)
