from operator import mul
from functools import reduce
from math import factorial
n = int(input())
s = str(n)
ans = 0
a = [s.count(str(digit)) for digit in range(10)]


def get(*args):
    res = factorial(sum(args))
    for x in args:
        res //= factorial(x)
    return res


for a0 in range(0 if not a[0] else 1, a[0] + 1):
    for a1 in range(0 if not a[1] else 1, a[1] + 1):
        for a2 in range(0 if not a[2] else 1, a[2] + 1):
            for a3 in range(0 if not a[3] else 1, a[3] + 1):
                for a4 in range(0 if not a[4] else 1, a[4] + 1):
                    for a5 in range(0 if not a[5] else 1, a[5] + 1):
                        for a6 in range(0 if not a[6] else 1, a[6] + 1):
                            for a7 in range(0 if not a[7] else 1, a[7] + 1):
                                for a8 in range(0 if not a[8] else 1, a[8] + 1):
                                    for a9 in range(0 if not a[9] else 1, a[9] + 1):
                                        ans += get(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
                                        if a0:
                                            ans -= get(a0 - 1, a1, a2, a3, a4, a5, a6, a7, a8, a9)
print(ans)
