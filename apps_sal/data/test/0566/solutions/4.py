"""
Codeforces Contest 273 Div 2 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""


import itertools


def main():
    a = read()
    a.sort()
    res = 0
    if a[1] - a[0] <= a[2] - a[1]:
        res += a[1] - a[0]
        a[1] -= res
        a[2] -= 2 * res
        if 4 * a[0] <= a[2]:
            print(res + 2 * a[0])
            return
        else:
            n = (a[2] - a[0]) // 3
            res += 2 * n
            a[0] -= n
            a[1] -= n
            a[2] -= 4 * n
            if 0 < a[0] == a[2] - 2:
                res += 1
                a[0] -= 1
                a[2] -= 2
            print(res + a[0])
            return
    else:
        res += a[2] - a[1]
        a[1] -= res
        a[2] -= 2 * res
        n = (a[1] - a[0]) // 3
        res += 2 * n
        a[1] -= 3 * n
        a[2] -= 3 * n
        if a[1] == a[0] + 2:
            res += 1
            a[1] -= 2
            a[2] -= 1
        print(res + a[0])
        return

# NON-SOLUTION STUFF BELOW


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


write(main())
