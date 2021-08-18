
import sys
from collections import Counter


def read_ints(inp=sys.stdin):
    return list(map(int, next(inp).strip().split()))


def print_list(l):
    print(' '.join(map(str, l)))


def sol1(A):
    A = A.lstrip("0")
    cc = Counter(A)
    res = cc['0'] >= 6
    return "yes" if res else "no"


def __starting_point():
    for i in range(1):
        A = next(sys.stdin).strip()
        print(sol1(A))


__starting_point()
