# -*- coding: utf-8 -*-
"""
@author: Saurav Sihag
"""

from sys import stdin, stdout, setrecursionlimit
def rr(): return input().strip()
def rri(): return int(rr())
# rri = lambda: int(stdin.readline())
def rrm(): return [int(x) for x in rr().split()]
# stdout.write(str()+'\n')


def sol():
    n = rri()
    res = ""
    if n == 1:
        print("8")
        return
    if n == 2:
        print("98")
        return

    z = (n + 4 - 1) // 4
    res = '9' * (n - z) + '8' * z
    print(res)
    return

# sol()


def main():
    T = rri()
    for t in range(1, T + 1):
        ans = sol()
        # print("Case #{}: {}".format(t, ans))


main()
