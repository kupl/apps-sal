
import sys
import bisect
from collections import Counter


def read_int(): return int(sys.stdin.readline())
def read_ints(): return list(map(int, sys.stdin.readline().split()))
def read_int_list(): return list(read_ints())
def read(): return sys.stdin.readline().strip()
def read_list(): return sys.stdin.readline().split()


def main():
    n, k = read_ints()
    s = read()
    d = Counter(s)
    res = k * min(d.values()) if len(d) == k else 0
    print(res)


main()
