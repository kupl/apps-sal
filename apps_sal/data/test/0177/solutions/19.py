import sys
import math


def read_int():
    return int(sys.stdin.readline().strip())


def read_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def read_string():
    return sys.stdin.readline().strip()


def read_string_list(delim=' '):
    return sys.stdin.readline().strip().split(delim)


seq = ''
for i in range(1, 3000):
    seq += str(i)
print(seq[read_int() - 1])
