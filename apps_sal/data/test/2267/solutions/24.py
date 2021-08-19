from sys import stdin
from functools import cmp_to_key


def input():
    return stdin.readline()


def mysort(x, y):
    return 1 if x + y > y + x else -1


n = int(input())
strings = []
for i in range(n):
    t = input().strip('\n')
    strings.append(t)
strings.sort(key=cmp_to_key(mysort))
print(''.join(strings))
