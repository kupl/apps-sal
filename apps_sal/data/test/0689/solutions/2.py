import math


def main():
    n = int(input())
    dct = dict()
    for i in range(n):
        s = input()
        for k in s:
            if k in dct:
                dct[k] += 1
            else:
                dct[k] = 1
    for i in dct:
        if dct[i] % n != 0:
            print("NO")
            return
    print("YES")

def __starting_point():
    t = int(input())

    for i in range(t):
        main()
"""
60, 61
"""
"""
"""

__starting_point()
