import sys
import math


def read_int():
    return int(input().strip())


def read_int_list():
    return list(map(int, input().strip().split()))


def read_string():
    return input().strip()


def read_string_list(delim=' '):
    return input().strip().split(delim)


def sumup(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


n = read_int()
locs = []
deltas = []
for _ in range(n):
    locs.append(tuple(read_int_list()))
for _ in range(n):
    deltas.append(tuple(read_int_list()))
locs.sort()
deltas.sort(reverse=True)
ans = sumup(locs[0], deltas[0])
print(ans[0], ans[1])
